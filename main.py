"""
Fox Utilities > main.py
Author: Feven Kitsune <fevenkitsune@gmail.com>
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
"""

# Imports
import discord
from discord.ext import commands
from ext.globals import *
import ext.exception as exception

import logging
from google.cloud import logging as cloudlog

# Object Setup
cloudlog_client = cloudlog.Client()
handler = cloudlog_client.get_default_handler()
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
client = commands.Bot(description=BOT_DESCRIPTION, command_prefix=BOT_PREFIX)

# Startup
@client.event
async def on_ready():
    logger.info("Setting client presence.")
    await client.change_presence(activity=discord.Game(BOT_DEFAULT_STATUS))
    logger.info("Fox Utilities is now ready!")

# Extension Loading
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
