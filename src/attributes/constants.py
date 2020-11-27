#
# # attributes/constants.py, Created by Janrey "CodexLink" Licas
# * To be used with cogs/** and entrypoint.py.

from discord import ActivityType
from typing import Final
import discord

## Rich Presence Activity
RP_ATTRS_DEFAULT: Final = {
    "RP_APP_ID": "NA",
    "RP_NAME": "with Listeners, ready.",
    "RP_TYPE": ActivityType.playing,
    "RP_STATE": "Unknown",
    "RP_DETAILS": "Unknown",
    "RP_TIMESTAMPS": {
        "TIMESTAMPT_START": "Dynamic",
        "TIMESTAMPT_END": 0,
    },
    "RP_ASSETS": {
        "ASSET_LARGE_IMAGE": "RectangleLargeKey",
        "ASSET_LARGE_TEXT": "LargeCircularIcon",
        "ASSET_SMALL_IMAGE": "CircularSmallKey",
        "ASSET_SMALL_TEXT": "Small Circular Icon",
    },
    "RP_IMAGE_TEXTS": {
        "LARGE_IMAGE_TEXT": "Large Image Text",
        "SMALL_IMAGE_TEXT": "Small Image Description",
    },
}

RP_NAME_MODES: Final = {
    "DATABASE_CHANGES_CHECK_1": (
        discord.Status.dnd,
        ActivityType.watching,
        "the Changes.",
    ),
    "DATABASE_CHANGES_CHECK_2": (
        discord.Status.dnd,
        ActivityType.watching,
        "All Changes.",
    ),
    "DATABASE_VALIDATION": (
        discord.Status.online,
        ActivityType.playing,
        "By Validating Data.",
    ),
    "PURELY_MAINTAINANCE": (
        discord.Status.idle,
        ActivityType.watching,
        "Maintainance Mode.",
    ),  # Omitted 'Profiles' string.
    "INITIAL_READY": (discord.Status.online, ActivityType.watching, "Ready."),
    "INITIAL_IDLE": (discord.Status.online, ActivityType.watching, "Currently Idle."),
    "INITIAL_LOADED_STATS_1": (
        discord.Status.online,
        ActivityType.playing,
        "with Github Profiles!",
    ),
    "INITIAL_LOADED_STATS_2": (
        discord.Status.online,
        ActivityType.watching,
        "{0}{1} Github Profiles!",
    ),
}


# # Bot Entrypoint Constants
PREFIX_COMMAND: Final = "."
ON_READY_MESSAGE: Final = """
Discord Boilerplate with Cogs in Set (Context Async Functions Unavailable)
Created by Janrey Licas

Currently Logged on as
"""

COGS_DIR_NAME = "cogs"
