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
@bot.tree.command(name="hello", description="Say hi to MalCheckerBot!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hey {interaction.user}! MOOOOOooooooOOOOOOOOOO!")


@bot.tree.command(name="useless_command")
async def useless(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"You really have nothing else to do... do you?!")


@bot.tree.command(name="help", description="Kinda self explanatory.")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"If your using this command for such a simple bot you truly DO need help. I would recommend starting out here: https://www.betterhelp.com"
    )


@bot.tree.command(
    name="mal_check",
    description=
    "Scientists have spend centuries working up a formula to isolate the Mal Gene. They found it!"
)
async def mal(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(
        responses.handle_response(user=member.name))
