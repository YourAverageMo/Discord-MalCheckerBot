import os

import discord
from discord.ext import commands
from dotenv import find_dotenv, load_dotenv

import responses

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
TOKEN = os.getenv("TOKEN")

# ------------ INTENTS ARE REQUIRED BY DISCORD
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


# ------------ INIT BOT
def run_discord_bot():
    """Called in main.py. Starts bot
    """
    bot.run(TOKEN)


@bot.event
async def on_ready():
    """When bot is initialized prints out bot is ready and also syncs all bot commands
    """
    print(f"{bot.user} is now running!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


# ------------ BOT COMMANDS
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hey {interaction.user}! this is a slash command!")


@bot.tree.command(name="useless_command")
async def useless(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"You really have nothing else to do... do you?!")
