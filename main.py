import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import discord.utils
import functools
from discord.utils import get
import math
import os
import utils
import random
import warnings
import datetime
from datetime import datetime, timedelta
from platform import python_version
from replit import db
from time import time
import discord
from discord.ext import commands, tasks
from io import BytesIO
import datetime
from datetime import datetime
from discord.ext import commands
import psutil
from psutil import Process, virtual_memory
import time
import pyfiglet
from psutil import Process, virtual_memory
intents=discord.Intents.default()

from PIL import Image
from io import BytesIO

intents.members=True

client = commands.Bot(command_prefix='>',case_insensitive=True,intents=intents)
from io import BytesIO

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')
@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel Unlocked.')
@lock.error
async def unlock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

 
@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
   client.load_extension(f'cogs.{extension}')
   await ctx.send('Succesfully loaded module')


@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
   client.unload_extension(f'cogs.{extension}')
   await ctx.send('Succesfully unloaded module')
  
@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
   client.reload_extension(f'cogs.{extension}')
   await ctx.send('Succesfully reloaded module')
   
class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(CogName(bot))

client.run(" ") #add your token here
