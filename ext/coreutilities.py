"""
Fox Utilities > coreutilities.py
Author: Feven Kitsune <fevenkitsune@gmail.com>
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
"""

# Imports
from ext.checks import *


class CoreUtilities(commands.Cog):
    """
    CoreUtilities class

    Core system operation commands.
    """

    def __init__(self, client):
        self.client = client

    @commands.command(
        name="help",
        brief="Display this message.",
        usage=""
    )
    async def help(self, ctx, *args):
        # Setup embed
        em = discord.Embed(color=message_color)
        em.set_footer(text=f"Invoked by: {ctx.message.author.name}")

        # Command
        for cmd in sorted(self.client.commands, key=lambda command: command.cog_name):
            if cmd.hidden and not (ctx.author.id == developer_id):
                pass  # If not developer, do not show hidden commands.
            else:
                em.add_field(
                    name=f"{'#' if cmd.hidden else ''}`{cmd.cog_name}`> {cmd.name} {cmd.usage}",
                    value=cmd.brief,
                    inline=False
                )  # Help field formatter.

        await ctx.author.send(embed=em)

    @commands.command(
        name="tags",
        brief="Information about bot-permission tags.",
        usage=""
    )
    async def tags(self, ctx, *args):
        # Setup embed
        em = discord.Embed(
            title="Fox Utilities Permission Tags",
            description="Create a role with the syntax `fox:name_of_command` to give them permission to access that command! Will work with any admin command!",
            color=message_color)
        em.set_footer(text=f"Invoked by: {ctx.message.author.name}")

        await ctx.send(embed=em)


# Extension setup
def setup(client):
    client.add_cog(CoreUtilities(client))
