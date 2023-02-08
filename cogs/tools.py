import argparse
import discord
import os
import platform
import re
import requests
import sys
import urllib.parse

from base64 import b64decode
from discord.ext import commands
from urllib.request import urlopen, Request

class Tools(commands.Cog):

    """Cog for Tools commands"""

    def __init__(self, bot):
        self.bot = bot
        
    #Adfly Command
    @commands.command(pass_context=True)
    async def adfly(self, ctx, search):
        if "http" not in search:
            search = "https://" + search
        req = Request(search, headers={'User-Agent': 'Chrome/91.0.4472.77'})
        data_ = urlopen(req)
        data = data_.read()
        ysmm = data.split(b"ysmm = '")[1].split(b"';")[0]
        decrypted_url = ysmm.decode('utf-8') # Decrypt the URL

        zeros, ones = '', ''
        for num, letter in enumerate(decrypted_url):
            if num % 2 == 0: zeros += decrypted_url[num]
            else: ones = decrypted_url[num] + ones

        key = list(zeros + ones)
        i=0
        while i != len(key):
            hlp=0
            if str(key[i]).isnumeric():
                for y in range(i+1,len(key)):
                    if str(key[y]).isnumeric():
                        hlp=hlp+1
                        temp=int(key[i])^int(key[y])
                        if int(temp) < 10:
                            key[i]=str(temp)
                        i=y+1
                        break
            if hlp==0:
                i=i+1
        temp="".join(key)
        key=temp
        key = b64decode(key.encode("utf-8"))

        decrypted_url=key[16:-16]
        decrypted_url = urllib.parse.unquote(decrypted_url)
        try:
            m = re.search ( r'&dest=(.*)', decrypted_url)
            decrypted_url = m.group(1)
        except:
            pass
        embed = discord.Embed(
            title=f"Adf.ly Decoder",
            description=decrypted_url,
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        try:
            embed.set_thumbnail(url="https://i.ibb.co/qJ0ZxTD/646023.png")
        except:
            pass
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #Technic Command
    @commands.command(pass_context=True)
    async def technic(self, ctx, search):
        url = "https://api.technicpack.net/search?q=" + search
        params = {
        'build': 'build',
        }
        responce = requests.get(url, params=params)
        json = responce.json()
        for pack in json["modpacks"]:
            url2 = "https://api.technicpack.net/modpack/" + pack["slug"]
            params2 = {
            'build': 'build',
            }
            packList = []
            responce = requests.get(url2, params=params)
            json2 = responce.json()
            finalURL = json2["url"]
            if finalURL == None:
                finalURL = "SOLDER MODPACK"
            packList.append("{}: {}".format(pack["slug"], finalURL))
        query = "\n".join(sorted(packList))
        if json["modpacks"] == []:
            query = "No Results"
            
        embed = discord.Embed(
            title=f"Technic Slug Lookup",
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        try:
            embed.set_thumbnail(url="https://i.ibb.co/qgXtt0Z/309359763-128793633250428-4428571622506032512-n.png")
        except:
            pass
        embed.add_field(name="Packs:", value=query, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Tools(bot))