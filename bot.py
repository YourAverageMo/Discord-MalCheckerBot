import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import find_dotenv, load_dotenv

import responses

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
TOKEN = os.getenv("TOKEN")

# ------------ INTENTS ARE REQUIRED BY DISCORD
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# ------------ SETTING UP BOT COMMANDS
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"{client.user} is now running!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hey {interaction.user.mention}! this is a slash command!")


if __name__ == "__main__":
    # run the bot
    bot.run(TOKEN)