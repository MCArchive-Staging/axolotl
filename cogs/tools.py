import argparse
import base64
import discord
import os
import platform
import re
import requests
import sys
import urllib.parse
import urllib.request

from base64 import b64decode
from discord.ext import commands
from urllib.request import urlopen, Request


class Tools(commands.Cog):

    """Cog for Tools commands"""

    def __init__(self, bot):
        self.bot = bot

    # Adfly Command
    @commands.command(pass_context=True)
    async def adfly(self, ctx, search):
        
        response = requests.head(search, allow_redirects=True)
        url = response.url

        print(url)
        
        parsed_url = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed_url.query)

        if "r" in query_params:
            decrypted_url = query_params["r"][0]
            decrypted_url2 = decrypted_url[:-1]
            print(decrypted_url2)
            # Add padding if needed
            while len(decrypted_url2) % 4 != 0:
                decrypted_url2 += "="
            decoded_string = base64.b64decode(decrypted_url2)
            decoded_string = decoded_string.decode(encoding='utf-8')


        else:
            decoded_string = "Invalid URL"

        embed = discord.Embed(
            title=f"Adf.ly Decoder",
            description=decoded_string,
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        try:
            embed.set_thumbnail(url="https://i.ibb.co/qJ0ZxTD/646023.png")
        except:
            pass
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    # Technic Command
    @commands.command(pass_context=True)
    async def technic(self, ctx, search):
        url = "https://api.technicpack.net/search?q=" + search
        params = {
            "build": "build",
        }
        responce = requests.get(url, params=params)
        json = responce.json()
        packList = []
        embed = discord.Embed(
            title=f"Technic Slug Lookup",
            description="\uFEFF",
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        try:
            for pack in json["modpacks"]:
                url2 = "https://api.technicpack.net/modpack/" + pack["slug"]
                params2 = {
                    "build": "build",
                }
                responce = requests.get(url2, params=params)
                json2 = responce.json()
                finalURL = json2["url"]
                if finalURL == None:
                    finalURL = "SOLDER MODPACK"
                embed.add_field(name=pack["name"], value=finalURL, inline=True)
            if json["modpacks"] == []:
                query = "No Results"
        except:
            pass
        try:
            embed.set_thumbnail(
                url="https://i.ibb.co/qgXtt0Z/309359763-128793633250428-4428571622506032512-n.png"
            )
        except:
            pass
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)
    
    # ATLauncher Search Command
    @commands.group(pass_context=True)
    async def atlaunch(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('**Subcommands:** file, md5, sha1, sha512')

    # ATLauncher Search Command
    @atlaunch.command(pass_context=True)
    async def file(self, ctx, jarfile):
        url = "https://api.atlauncher.com/v1/file-lookup"
        json = {
            "filename": jarfile,
        }
        headers = {
        'User-Agent': 'MCArchive: Axolotl Bot. https://discord.gg/WuexGpP',
        }
        responce = requests.post(url, json=json, headers=headers)
        
        json = responce.json()
        modList = []
        embed = discord.Embed(
            title=f"ATLauncher Mod Lookup",
            description="\uFEFF",
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        for pack in json:
            embed.add_field(name=json[0]['mod_name'], value=json[0]['friendly_url'], inline=True)
        if json == []:
            embed.add_field(name='Error', value="No Results", inline=True)
        embed.set_thumbnail(url="https://i.ibb.co/GFJtgNy/atlauncher-208731.webp")
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)
    
    # ATLauncher Search Command
    @atlaunch.command(pass_context=True)
    async def md5(self, ctx, jarfile):
        url = "https://api.atlauncher.com/v1/file-lookup"
        json = {
            "md5": jarfile,
        }
        headers = {
        'User-Agent': 'MCArchive: Axolotl Bot. https://discord.gg/WuexGpP',
        }
        responce = requests.post(url, json=json, headers=headers)
        
        json = responce.json()
        modList = []
        embed = discord.Embed(
            title=f"ATLauncher Mod Lookup",
            description="\uFEFF",
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        for pack in json:
            embed.add_field(name=json[0]['mod_name'], value=json[0]['friendly_url'], inline=True)
        if json == []:
            embed.add_field(name='Error', value="No Results", inline=True)
        embed.set_thumbnail(url="https://i.ibb.co/GFJtgNy/atlauncher-208731.webp")
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)
    
    # ATLauncher Search Command
    @atlaunch.command(pass_context=True)
    async def sha1(self, ctx, jarfile):
        url = "https://api.atlauncher.com/v1/file-lookup"
        json = {
            "sha1": jarfile,
        }
        headers = {
        'User-Agent': 'MCArchive: Axolotl Bot. https://discord.gg/WuexGpP',
        }
        responce = requests.post(url, json=json, headers=headers)
        
        json = responce.json()
        modList = []
        embed = discord.Embed(
            title=f"ATLauncher Mod Lookup",
            description="\uFEFF",
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        for pack in json:
            embed.add_field(name=json[0]['mod_name'], value=json[0]['friendly_url'], inline=True)
        if json == []:
            embed.add_field(name='Error', value="No Results", inline=True)
        embed.set_thumbnail(url="https://i.ibb.co/GFJtgNy/atlauncher-208731.webp")
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)
    
    # ATLauncher Search Command
    @atlaunch.command(pass_context=True)
    async def sha512(self, ctx, jarfile):
        url = "https://api.atlauncher.com/v1/file-lookup"
        json = {
            "sha512": jarfile,
        }
        headers = {
        'User-Agent': 'MCArchive: Axolotl Bot. https://discord.gg/WuexGpP',
        }
        responce = requests.post(url, json=json, headers=headers)
        
        json = responce.json()
        modList = []
        embed = discord.Embed(
            title=f"ATLauncher Mod Lookup",
            description="\uFEFF",
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        for pack in json:
            embed.add_field(name=json[0]['mod_name'], value=json[0]['friendly_url'], inline=True)
        if json == []:
            embed.add_field(name='Error', value="No Results", inline=True)
        embed.set_thumbnail(url="https://i.ibb.co/GFJtgNy/atlauncher-208731.webp")
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    # ATLauncher Search Command
    @commands.group(pass_context=True)
    async def modrinth(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('**Subcommands:** sha1, sha512')
    
    # Modrinth Search Command
    @modrinth.command(pass_context=True)
    async def sha1(self, ctx, jarfile):
        url = "https://api.modrinth.com/v2/version_file/" + jarfile
        headers = {
        'User-Agent': 'MCArchive: Axolotl Bot. https://discord.gg/WuexGpP',
        }
        params = {
            "alogrithm": "sha1",
        }
        responce = requests.get(url, headers=headers, params=params)
        
        json = responce.json()
        modList = []
        embed = discord.Embed(
            title=f"ATLauncher Mod Lookup",
            description="\uFEFF",
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(name=json['files'][0]['filename'], value=json['files'][0]['url'], inline=True)
        if json == []:
            embed.add_field(name='Error', value="No Results", inline=True)
        embed.set_thumbnail(url="https://i.ibb.co/GFJtgNy/atlauncher-208731.webp")
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)
    
    # Modrinth Search Command
    @modrinth.command(pass_context=True)
    async def sha512(self, ctx, jarfile):
        url = "https://api.modrinth.com/v2/version_file/" + jarfile
        headers = {
        'User-Agent': 'MCArchive: Axolotl Bot. https://discord.gg/WuexGpP',
        }
        params = {
            "alogrithm": "sha512",
        }
        responce = requests.get(url, headers=headers, params=params)
        
        json = responce.json()
        modList = []
        embed = discord.Embed(
            title=f"ATLauncher Mod Lookup",
            description="\uFEFF",
            colour=0x98FB98,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(name=json['files'][0]['filename'], value=json['files'][0]['url'], inline=True)
        if json == []:
            embed.add_field(name='Error', value="No Results", inline=True)
        embed.set_thumbnail(url="https://i.ibb.co/GFJtgNy/atlauncher-208731.webp")
        embed.set_footer(
            text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)



def setup(bot):
    bot.add_cog(Tools(bot))
