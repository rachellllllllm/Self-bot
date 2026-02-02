import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import random

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Selfbot setup - user account mode
bot = commands.Bot(command_prefix=".", self_bot=True, help_command=None)

@bot.event
async def on_ready():
    print(f"Selfbot logged in as {bot.user} (ID: {bot.user.id})")
    print("Spam mode ready - use .startspam in a channel to begin")

# Command to start spamming /fish1 (or whatever slash command)
@bot.command()
async def startspam(ctx, count: int = 100, delay_min: float = 5.0, delay_max: float = 10.0):
    """
    Starts spamming the /fish1 slash command in the current channel.
    Usage: .startspam [count] [min_delay] [max_delay]
    Example: .startspam 50 30 60  → spams 50 times with random 30-60s delays
    """
    if count <= 0:
        await ctx.send("Count must be positive.")
        return

    await ctx.send(f"Starting spam of /fish1 - {count} times with random delays {delay_min}-{delay_max}s")

    for i in range(count):
        try:
            # Spam the slash command /fish1
            # If it's actually /fish or something else, change 'fish1' below to match
            await ctx.channel.send_slash(
                name="fish1",  # <-- Change this to the exact slash command name, e.g. "fish" for Virtual Fisher
                options={}     # Add options if the command needs args, e.g. {"bait": "worm"}
            )
            print(f"Sent /fish1 spam #{i+1}/{count}")
        except Exception as e:
            print(f"Error sending spam: {e}")
            await ctx.send(f"Spam error at #{i+1}: {str(e)}")
            break

        # Random human-like delay to avoid instant detection
        wait_time = random.uniform(delay_min, delay_max)
        await asyncio.sleep(wait_time)

    await ctx.send("Spam finished.")

# Optional: Stop command if needed (just restart the host to kill)
@bot.command()
async def stopspam(ctx):
    await ctx.send("Stopping spam loop (restart host to fully kill).")

# Run the selfbot
bot.run(TOKEN, bot=False)
