from discord.ext import commands
from discord.ext.commands import bot

import discord
import random
import time
import os

bot = commands.Bot(command_prefix="!")

@bot.command()
async def randomNbr(ctx, x, y):
    await ctx.send(random.randint(x, y))

#.env file required (TOKEN)
bot.run(os.getenv("TOKEN"))