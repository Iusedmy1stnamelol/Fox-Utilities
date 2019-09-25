"""
Fox Utilities > main.py
Author: Feven Kitsune <fevenkitsune@gmail.com>
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
"""

# Imports
import discord
from discord.ext import commands
import logging

# Program Imports
from ext.globals import *
from ext.checks import get_prefix
import ext.exception as exception

# Logging
logger = logging.getLogger("discord")  # Set up logger called "discord"
logger.setLevel(logging.INFO)  # Log all

# Client
client = commands.Bot(description=BOT_DESCRIPTION, command_prefix=get_prefix)


# Executes once the bot has finished starting.
@client.event
async def on_ready():
    logger.info(f"Setting client presence to: {BOT_DEFAULT_STATUS}")
    await client.change_presence(activity=discord.Game(BOT_DEFAULT_STATUS)) # Set the bot status
    logger.info("Fox Utilities is now ready!")


# Bot setup and loading
if __name__ == "__main__":
    # Remove default help command, this is replaced in coreutilities.
    logger.info("Removing default help command.")
    client.remove_command("help")

    # Register exception.py as the exception handler.
    logger.info("Registering error handler.")
    client.add_listener(exception.on_command_error)

    # External cogs
    for extension in extensions:
        try:
            client.load_extension(extension)  # Load all extensions
        except Exception as e:  # If load failed, post to log.
            exc = f"{type(e).__name__}: {e}"
            logger.warning(f"Failed to load extension {extension}\n{exc}")
        else:  # If load succeeded, post to log.
            logger.info(f"Loaded extension {extension}")

    # Start Bot
    logger.info("Starting client.")
    client.run(BOT_KEY)  # Start server.
