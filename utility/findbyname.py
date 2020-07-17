"""
Fox Utilities > findbyname.py
Author: Feven Kitsune <fevenkitsune@gmail.com>
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
"""

from discord.utils import find
from fuzzywuzzy.process import extract
from unicodedata import normalize


async def find_by_name(name, search_in):
    """Performs a fuzzy search with unicode-font conversions."""
    # found_name = process.extractOne(normalize("NFKC", name), [normalize("NFKC", item.name) for item in search_in])
    # TODO SET THIS BACK TO NORMAL
    found_name = extract(normalize("NFKC", name), [normalize("NFKC", item.name) for item in search_in], limit=3)
    # found_item = find(lambda m: normalize("NFKC", m.name) == found_name[0], search_in)
    found_item = [find(lambda m: normalize("NFKC", m.name) == found, search_in) for found in found_name]
    raise UserWarning("Testing")
    return found_name  # returning non-matched array first because extract() returns tuple
