#***************************************************************************#
#                                                                           #
# Background Axolotl                                                        #
# https://github.com/EndangeredNayla/Axolotl                                #
# Copyright (C) 2023 Nayla Hanegan. All rights reserved.                    #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#
import discord
import os
import platform

from cogs.base import Base
from cogs.fun import Fun
from cogs.minecraft import Minecraft
from cogs.tools import Tools

from discord.ext import tasks
from discord.ext import commands

#Intents
intents = discord.Intents.all()

#Define Client
bot = commands.Bot(description="Background Axolotl", command_prefix=commands.when_mentioned_or("?"), intents=intents, activity=discord.Game(name='Miencraft'))

@bot.event
async def on_ready():
  memberCount = len(set(bot.get_all_members()))
  serverCount = len(bot.guilds)
  print("                                          ")
  print("##########################################") 
  print(f"                ⣀⣀⡤⠤⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ")
  print(f"  ⠀⠀⢴⠋⠙⠳⣤⡀⣠⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠓⠤⡀⣠⡴⠟⠛⣷⠀⠀   ")
  print(f"  ⠀⠀⠈⠳⢤⣀⢈⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ara⠘⢏⣀⣠⡴⠋⠀⠀   ")
  print(f"  ⢀⣠⣤⣄⣄⣉⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⣡⣤⡴⣦⣀   ")
  print(f"  ⢹⣅⡀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠁⠀⢀⣠⠏   ")
  print(f"  ⠀⠈⠙⠉⢋⣉⣇⠀⠀⣾⣷⠄⠀⠀⠀⠀⠀⠀⠀⢴⣿⡆⠀⢀⣿⡙⠋⠋⠀⠀   ")
  print(f"  ⠀⠀⢤⠶⠋⠉⢈⣦⡀⠈⠉⠀⠀⠀⠉⠉⠉⠀⠀⠀⠉⠀⣠⣎⠈⠉⠛⢷⡀⠀   ")
  print(f"  ⠀⠀⠻⣤⣤⠶⠋⠀⠈⠑⠠⠄⣀⣀⣀⣀⣀⣀⡀⠤⠐⠉⠀⠈⠻⠶⠖⠶⠃⠀   ")
  print(f"  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠤⡀⠀⡠⠤⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
  print(f"  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠉⠁⠀⠉⠉⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
  print(f"  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢀⠤⡀⠀⡠⢄⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
  print(f"  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠢⣀⣀⣀⣈⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
  print(f"  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⡇⠀⣎⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
  print(f"  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⡇⣸⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
  print(f"  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
  print("##########################################") 
  print("Running as: " + bot.user.name + "#" + bot.user.discriminator)
  print(f'With Client ID: {bot.user.id}')
  print("\nBuilt With:")
  print("Python " + platform.python_version())
  print("Py-Cord " + discord.__version__)

#Boot Cogs
bot.add_cog(Base(bot))
bot.add_cog(Fun(bot))
bot.add_cog(Minecraft(bot))
bot.add_cog(Tools(bot))

#Run Bot
TOKEN = os.environ.get("TOKEN_AXOLOTL")
bot.run(TOKEN)