"""
Fox Utilities > checks.py
Author: Feven Kitsune <fevenkitsune@gmail.com>
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
"""

import discord
from discord.ext import commands
from ext.globals import *

def has_tag():
    async def predicate(ctx):
        return (
            True if discord.utils.get(ctx.author.roles, name=str(role_tag[ctx.command.name])) is not False
        )
    return commands.check(predicate)

def is_admin():
    async def predicate(ctx):
        return (
            ctx.message.channel.permissions_for(ctx.message.author).administrator
            or (ctx.author.id == DEV_ID)  # Permissions for dev.
        )
    return commands.check(predicate)


def is_developer():
    async def predicate(ctx):
        return (
            ctx.author.id == DEV_ID
        )
    return commands.check(predicate)
