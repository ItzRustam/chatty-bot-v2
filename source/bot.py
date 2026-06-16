from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import asyncio
from llm_integreation.mini_llama import generate

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# Step 1: Set up intents to read message content
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
activity = discord.Activity(type=discord.ActivityType.playing, name="MineCraft")

@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')
    await client.change_presence(activity=activity, status=discord.Status.idle)

# Step 2: Initialize the bot with a command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# Step 3: Define the !ping command
@bot.command()
async def chat(ctx):
    if ctx.author == bot.user:
        return  # avoid responding to itself
    msg = ctx.message.content
    
    
    response = generate(msg.lower())
    await ctx.reply(response)

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return

    # Check if the bot was mentioned in the message
    if bot.user.mentioned_in(message):
        # Extract the text and remove the bot mention from the string
        clean_text = message.content.replace(f"<@{bot.user.id}>", "").strip()
        
        response = generate(clean_text)

        # Reply directly to the user who sent it
        await message.reply(response)

    # Required to let other bot commands run normally
    await bot.process_commands(message)

# Step 4: Run the bot with your token
bot.run(TOKEN)