"""
Fox Utilities > misctools.py
Author: Feven Kitsune <fevenkitsune@gmail.com>
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
"""

# Imports
from ext.checks import *


class MiscTools(commands.Cog):
    """
    MiscTools class

    Miscellaneous commands and utilities.
    """

    def __init__(self, client):
        self.client = client


# Extension setup
def setup(client):
    client.add_cog(MiscTools(client))
