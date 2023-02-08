import aiohttp
import discord
import random
import box

from dadjokes import Dadjoke
from discord.ext import commands

class Fun(commands.Cog):

    """Cog for Fun commands"""

    def __init__(self, bot):
        self.bot = bot
    
    #Roll Command
    @commands.command()
    async def roll(self, ctx, min=1, max=6, count=1):
        """Roll some dice, min, max, dice_count, defaults to 1d6"""
        if count <= 20:
            for _ in range(count):
                await ctx.send(random.randint(min, max))
        if count > 20:
            await ctx.send('Invalid number of rolls')

    #Dadjoke Command
    @commands.command(aliases=["dadjoke"])
    async def joke(self, ctx):
        """Sends the dadjokes"""
        async with ctx.typing():
            await ctx.send(Dadjoke().joke)

    #Coin Flip Command
    @commands.command(aliases=["flip"])
    async def toss(self, ctx):
        """Heads or tails"""
        ch = ["Heads", "Tails"]
        rch = random.choice(ch)
        await ctx.send(f"You got **{rch}**")


    #Reverse Text Command
    @commands.command()
    async def reverse(self, ctx, *, text):
        """Reverse the given text"""
        await ctx.send("".join(list(reversed(str(text)))))


    #Meme Command
    @commands.command()
    async def meme(self, ctx):
        """Sends you random meme"""
        r = await aiohttp.ClientSession().get(
            "https://www.reddit.com/r/dankmemes/top.json?sort=new&t=day&limit=100")
        r = await r.json()
        r = box.Box(r)
        data = random.choice(r.data.children).data
        img = data.url
        title = data.title
        url_base = data.permalink
        url = "https://reddit.com" + url_base
        embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
        embed.set_image(url=img)
        await ctx.send(embed=embed)


    #Reddit Wide Search Command
    @commands.command()
    async def reddit(self, ctx, meme_term):
        url_comb = "https://www.reddit.com/search.json?sort=newlimit=100&q=" + meme_term
        r = await aiohttp.ClientSession().get(url_comb)
        r = await r.json()
        r = box.Box(r)
        data = random.choice(r.data.children).data
        img = data.url
        title = data.title
        url_base = data.permalink
        url = "https://reddit.com" + url_base
        embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
        embed.set_image(url=img)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))