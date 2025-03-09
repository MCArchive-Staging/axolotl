import requests
import re
import base64
import time
from typing import Set, List

YSMM_PATTERN = re.compile(r"^.*ysmm\s*=\s*['\"](.+?)['\"];.*$", re.MULTILINE | re.DOTALL)

def get_with_retries(url, headers, retries=3, delay=5, proxies=None):
    """
    Fetches a URL with retries and a delay in case of failures.
    """
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10, proxies=proxies)
            if response.status_code == 200:
                return response
            else:
                print(f"Attempt {i+1}: Received status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i+1}: Request failed - {e}")
        time.sleep(delay)
    return None

def skip(adfly: str) -> Set[str]:
    """
    Returns possible decodings of the given adf.ly link using data from the WaybackMachine.
    """
    sns = get_wayback_snapshots(adfly)
    if not sns:
        raise Exception("Unavailable in WaybackMachine or Linkvertise!")
    
    ret = set()
    for sn in sns:
        body = get_wayback_body(sn)
        if body is None:
            continue
        ysmm = search_ysmm(body)
        if ysmm is None:
            continue
        try:
            ret.add(crack_ysmm(ysmm))
        except Exception:
            pass
        try:
            ret.add(crack_ysmm_old(ysmm))
        except Exception:
            pass
    
    if not ret:
        raise Exception("Cannot find ysmm!")
    
    return ret

def get_wayback_snapshots(url: str) -> List[str]:
    """
    Returns all the snapshots of the given URL that are archived within the WaybackMachine.
    """
    urls = []
    urls300 = []
    headers = {"Referer": f"https://web.archive.org/web/20240000000000*/{url}?output=json"}
    
    response = get_with_retries(f"https://web.archive.org/__wb/sparkline?output=json&url={url}&collection=web", headers)
    if response is None:
        return urls
    
    try:
        years = response.json().get('years', {}).keys()
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return urls
    
    for year in sorted(map(int, years)):
        response = get_with_retries(f"https://web.archive.org/__wb/calendarcaptures/2?url={url}&date={year}&groupby=day", headers)
        if response is None:
            continue
        
        try:
            days = response.json().get('items', [])
        except ValueError:
            continue

        for day_arr in days:
            day = f"{day_arr[0]:04d}"
            headers2 = {"Referer": f"https://web.archive.org/web/{year}{day}000000*/{url}"}
            response = get_with_retries(f"https://web.archive.org/__wb/calendarcaptures/2?url={url}&date={year}{day}", headers2)
            if response is None:
                continue
            
            try:
                times = response.json().get('items', [])
            except ValueError:
                continue
            
            for time_arr in times:
                time = f"{time_arr[0]:06d}"
                status = time_arr[1]
                if status // 100 == 2:
                    urls.append(f"https://web.archive.org/web/{year}{day}{time}/{url}")
                elif status // 100 == 3:
                    urls300.append(f"https://web.archive.org/web/{year}{day}{time}/{url}")

    urls.extend(urls300)
    return urls

def get_wayback_body(wayback_url: str) -> str:
    """
    Returns the archived body of the given WaybackMachine URL.
    """
    wb_url = wayback_url.replace("/http", "if_/http")
    response = get_with_retries(wb_url, {})
    if response:
        return response.text
    return None

def search_ysmm(body: str) -> str:
    """
    Searches and returns the ysmm within the given body.
    """
    match = YSMM_PATTERN.search(body)
    return match.group(1) if match else None

def crack_ysmm_old(ysmm: str) -> str:
    """
    Old method to decode a given ysmm.
    """
    left, right = [], []
    for i in range(0, len(ysmm), 2):
        left.append(ysmm[i])
        if i + 1 < len(ysmm):
            right.insert(0, ysmm[i + 1])
    decoded_uri = base64.b64decode(''.join(left) + ''.join(right)).decode('utf-8')[2:]
    decoded_uri = re.sub(r"go\.php\?u=", "", decoded_uri)
    return base64.b64decode(decoded_uri).decode('utf-8')

def crack_ysmm(ysmm: str) -> str:
    """
    JDownloader's approach to decode ysmm.
    """
    C, h = [], []
    for s in range(len(ysmm)):
        (C if s % 2 == 0 else h).append(ysmm[s])
    sec = base64.b64decode(''.join(C) + ''.join(h)).decode('utf-8')
    pcount = sec.find("http") if "http" in sec else sec.find("ftp")
    return sec[pcount:] if pcount > -1 else sec[16:-16]

# Example usage
if __name__ == "__main__":
    try:
        print(skip("http://adf.ly/W6VYO"))
    except Exception as e:
        print(f"Error: {e}")
