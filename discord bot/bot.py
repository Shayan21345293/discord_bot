import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am alive! 🤖")

bot.run(TOKEN)
