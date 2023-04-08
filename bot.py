import os
import discord
from dotenv import load_dotenv
from steamship import Steamship

# Load environment variables from the .env file
load_dotenv()

# Get the Steamship instance handle from the environment variable
instance_handle = os.getenv("INSTANCE_HANDLE")

# Instantiate the Steamship client
llm = Steamship.use("cartmangpt", instance_handle=instance_handle)

# Create a Discord client
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message mentions the bot
    if client.user in message.mentions:
        # Generate a response using Steamship
        input_message = f"User's Message: {message}"
        response = llm.invoke("generate", input=input_message)

        # Reply with the generated response
        await message.reply(response)


# Get the Discord bot token from the environment variable
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

client.run(discord_bot_token)
