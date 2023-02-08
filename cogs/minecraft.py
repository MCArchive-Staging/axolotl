import discord
import platform

from discord.ext import commands

class Minecraft(commands.Cog):

    """Cog for Minecraft commands"""

    def __init__(self, bot):
        self.bot = bot

    #Log Command
    @commands.command(ailases="upload_log")
    async def log(self, ctx):
        embed = discord.Embed(
            title=f"Please upload your log!",
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        try:
            embed.set_thumbnail(url="https://i.ibb.co/NjJKF58/log.png")
        except:
            pass
        embed.set_image(url="https://cdn.discordapp.com/attachments/531598137790562305/575381000398569493/unknown.png")
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #Select Java Command
    @commands.command(ailases="select_java")
    async def sjava(self, ctx):
        embed = discord.Embed(
            title=f"Please select your Java version in the MultiMC/Prism settings",
            description='USE Java 8 FOR 1.16 and BELOW, USE Java 17+ for 1.17 and HIGHER',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        try:
            embed.set_thumbnail(url="https://i.ibb.co/NtKN38j/java-coffee-cup-logo-v1.png")
        except:
            pass
        embed.set_image(url="https://cdn.discordapp.com/attachments/531598137790562305/575378380573114378/unknown.png")
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #Select RAM Command
    @commands.command(ailases=["select_memory", "sram", "select_ram"])
    async def smemory(self, ctx):
        embed = discord.Embed(
            title=f"Please set your instance memory allocation",
            description='Allocating too much RAM to Minecraft is bad for performance. See <https://vazkii.notion.site/A-semi-technical-explanation-of-why-you-shouldn-t-allocate-too-much-RAM-to-Minecraft-78e7bd41ba6646de8d1c55c033674bce> for more info',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        try:
            embed.set_thumbnail(url="https://i.ibb.co/PrBmDFb/ram.png")
        except:
            pass
        embed.set_image(url="https://cdn.discordapp.com/attachments/531598137790562305/575376840173027330/unknown.png")
        embed.set_footer(text=f"Ran by: {ctx.message.author} • Yours truly, {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Minecraft(bot))