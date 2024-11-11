import requests
import re
import base64
from typing import Set, List

YSMM_PATTERN = re.compile(r"^.*ysmm\s*=\s*['\"](.+?)['\"];.*$", re.MULTILINE | re.DOTALL)

def skip(adfly: str) -> Set[str]:
    """
    Returns possible decodings of the given adf.ly link using data from the WaybackMachine.
    """
    sns = get_wayback_snapshots(adfly)
    if not sns:
        raise Exception("Unavailable in WaybackMachine!")
    
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

    headers = {
        "Referer": f"http://web.archive.org/web/20240000000000*/{url}?output=json"
    }

    response = requests.get(f"https://web.archive.org/__wb/sparkline?output=json&url={url}&collection=web", headers=headers)
    
    # Check if the response is valid
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.text}")
        return urls  # Return an empty list if there's an error

    try:
        years = response.json()['years'].keys()
    except ValueError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content: {response.text}")
        return urls  # Return an empty list if JSON decoding fails

    for year in sorted(map(int, years)):
        response = requests.get(f"http://web.archive.org/__wb/calendarcaptures/2?url={url}&date={year}&groupby=day")
        days = response.json()['items']

        for day_arr in days:
            day = f"{day_arr[0]:04d}"
            response = requests.get(f"http://web.archive.org/__wb/calendarcaptures/2?url={url}&date={year}{day}")
            times = response.json()['items']

            for time_arr in times:
                time = f"{time_arr[0]:06d}"
                status = time_arr[1]
                if status // 100 == 2:  # is 2XX status code? - OK
                    urls.append(f"http://web.archive.org/web/{year}{day}{time}/{url}")
                elif status // 100 == 3:  # is 3XX status code? - redirects
                    urls300.append(f"http://web.archive.org/web/{year}{day}{time}/{url}")

    urls.extend(urls300)
    return urls

def get_wayback_body(wayback_url: str) -> str:
    """
    Returns the archived body of the given WaybackMachine URL.
    """
    wb_url = wayback_url.replace("/http", "if_/http")
    try:
        response = requests.get(wb_url)
        return response.text
    except Exception:
        return None

def search_ysmm(body: str) -> str:
    """
    Searches and returns the ysmm within the given body.
    """
    match = YSMM_PATTERN.search(body)
    if match:
        return match.group(1)
    return None

def crack_ysmm_old(ysmm: str) -> str:
    """
    My manual "old" approach to decode a given ysmm.
    """
    left = []
    right = []

    for i in range(0, len(ysmm), 2):
        left.append(ysmm[i])
        if i + 1 < len(ysmm):
            right.insert(0, ysmm[i + 1])

    decoded_uri = base64.b64decode(''.join(left) + ''.join(right)).decode('utf-8')[2:]

    pattern = re.compile(r"go\.php\?u=")
    decoded_uri = pattern.sub("", decoded_uri)

    return base64.b64decode(decoded_uri).decode('utf-8')

def crack_ysmm(ysmm: str) -> str:
    """
    JDownloader's approach to decode a given ysmm.
    """
    C = []
    h = []

    for s in range(len(ysmm)):
        if s % 2 == 0:
            C.append(ysmm[s])
        else:
            h.insert(0, ysmm[s])

    sec = base64.b64decode(''.join(C) + ''.join(h)).decode('utf-8')
    pcount = sec.find("http")
    if pcount == -1:
        pcount = sec.find("ftp")
    
    if pcount > -1:
        finallink = sec[pcount:]
    else:
        finallink = sec[16:-16]

    return finallink

# Example usage
if __name__ == "__main__":
    print(skip("http://adf.ly/W6VYO"))