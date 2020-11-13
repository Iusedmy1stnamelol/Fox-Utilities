"""
Fox Utilities > help.py
Author: Feven Kitsune <fevenkitsune@gmail.com>
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
"""

import discord
from discord.ext import commands

from config.globals import bot_description, message_color, developer_id
from utils.generators import generate_footer


class Help(commands.Cog):
    """
    Help class

    Generates and outputs the help menu.
    """
    category = "info"

    def __init__(self, client):
        self.client = client

    @commands.command(
        name="help",
        brief="Display this message.",
        usage="[command]",
        help="The help command can be used to get a list of commands that are available to the user. "
             "If you'd like to see more detailed information about a command, use `help [command]`.\n\n"
             "**Usage Information**\n"
             "Certain commands will have extra information on "
             "[arguments](https://en.wikipedia.org/wiki/Command-line_interface#Arguments) you can give the command to"
             "operate it.\n\n"
             "*[argument]*: Arguments marked with [] are optional, and are not required.\n"
             "*argument*: Arguments without [] are required to use the command.\n"
             "*argument/\"argument\"*: Arguments separated with a slash delineate two ways of stating the same argument."
    )
    async def help(self, ctx, *args):
        """Help menu. Processes the list of available commands into a readable menu."""
        em = discord.Embed(
            title="Fox Utilities Help Guide",
            description=bot_description,
            color=message_color
        )
        em.set_footer(text=generate_footer(ctx))

        if args and (search := args[0]):
            # If there is an args list, assign variable search with the first value.
            # User is requesting information about a specific command.
            if command := self.client.get_command(search):
                # Search client for given command. Assign variable command with found value.
                # Command will be None if no command is found.
                em.add_field(
                    name=f"{'#' if command.hidden else ''}`{command.cog_name}`\n{command.name} {command.usage}",
                    value=f"{command.help}\n\n**Aliases**\n{command.aliases}"
                )
            else:
                # Variable command is None. Throw UserWarning.
                raise UserWarning(f"Command \"{args[0]}\" was not found.")
        else:
            # User did not provide a specific command to read about. Generate an overview of available commands.
            # Dictionary structure that will contain cogs sorted by their class attribute "category"
            # categories["category_name"] = [list of cogs that belong to that category]
            categories = {}
            for cog in [self.client.get_cog(cog_name) for cog_name in sorted(self.client.cogs)]:
                # Get discord.ext.commands.Cog object in alphabetical order.
                if not hasattr(cog, "category"):
                    # If the Cog object doesn't have a category class attribute, ignore it.
                    # This is useful for cogs containing only helper functions.
                    continue

                if cog.category not in categories:
                    # Cog category hasn't been seen before, create new key in categories dictionary.
                    categories[cog.category] = [cog]
                else:
                    # Cog category has been seen before, append to existing list in categories dictionary.
                    categories[cog.category].append(cog)

            for key in list(categories):
                # Get each key in the categories dictionary.
                command_list = []
                for cog in categories[key]:
                    # With each key, iterate through the cogs in that category and generate the appropriate embed field.
                    for command in cog.walk_commands():
                        if command.hidden and not (ctx.author.id == developer_id):
                            # Hide Developer commands.
                            continue
                        command_list.append(
                            f"{'#' if command.hidden else ''}"
                            f"`{' '.join((command.name, command.usage)).strip()}` {command.brief}"
                        )
                if command_list:
                    # There are commands in this category the user can access. Show this category.
                    em.add_field(name=key.capitalize(), value="\n".join(command_list), inline=False)
                else:
                    # The user has access to none of the commands in this category. Don't add an empty embed.
                    continue

        await ctx.author.send(embed=em)


def setup(client):
    """Register class with client object."""
    client.add_cog(Help(client))
