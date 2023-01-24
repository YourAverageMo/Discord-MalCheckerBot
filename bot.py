import os

import discord
from dotenv import find_dotenv, load_dotenv

import responses

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# intents are required by discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


async def send_message(message, user):
    try:
        response = responses.handle_response(user)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv("TOKEN")

    # start the bot
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    client.run(TOKEN)


# when bot recieves a meg
@client.event
async def on_message(message):
    if message.author == client.user:  #ignore msg from bot
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: {user_message} in {channel}")

    # use this line for setting bot commands
    # if user_message[0] == "?":
    await send_message(message, username)
