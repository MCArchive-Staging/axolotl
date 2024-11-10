import platform
import json
import requests
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tools(commands.Cog):

    """Cog for Tools commands"""

    def __init__(self, bot):
        self.bot = bot

    # Adfly Command
    @commands.command(pass_context=True)
    async def adfly(self, ctx, search):
        service = Service('chromedriver')

        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            hard_migrator_url = f"https://publisher.linkvertise.com/adfly-hard-migrator/url?url={search}"

            # Navigate to the hard migrator URL
            driver.get(hard_migrator_url)

            # Wait for the URL to change to any linkvertise URL
            WebDriverWait(driver, 5).until(lambda d: d.current_url.startswith("https://linkvertise.com/"))

            # Get the redirected URL
            url = driver.current_url
            print(f"Redirected URL: {url}")

            # Now, make a request to the bypass API using requests
            base_url = f"https://api.bypass.vip/bypass?url={url}"
            response = requests.get(base_url)

            # Check if the request was successful
            if response.status_code == 200:
                response_json = response.json()  # Parse the JSON response
                
                # Extract the bypassed URL
                if response_json.get("status") == "success":
                    bypassed_url = response_json.get("result")
                    embed = discord.Embed(
                        title="Adf.ly Decoder",
                        description=bypassed_url,
                        colour=0x98FB98,
                        timestamp=ctx.message.created_at,
                    )
                    embed.set_footer(
                        text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}"
                    )
                    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Failed to retrieve the bypassed URL. Error: {response_json.get('message')}")
            else:
                await ctx.send(f"Failed to call the bypass API. Status code: {response.status_code}")

        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

        finally:
            driver.quit()  # Close the browser
    
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
