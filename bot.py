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


def run_discord_bot():
    # start the bot
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    client.run(TOKEN)



# ------------ BOT FUNCTIONS
async def send_message(message, user):
    try:
        response = responses.handle_response(user)
        await message.channel.send(response)
    except Exception as e:
        print(e)


# ------------ WHEN BOT RECEIVES A MSG
# @client.event
# async def on_message(message):
#     if message.author == client.user:  #ignore msg from bot
#         return

#     username = str(message.author)
#     user_message = str(message.content)
#     channel = str(message.channel)

#     print(f"{username} said: {user_message} in {channel}")
#     await send_message(message, username)


# ------------ BOT COMMANDS
@bot.command()
async def ping(ctx):
    await ctx.send("pong")