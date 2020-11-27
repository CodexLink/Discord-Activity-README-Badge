#
# # attributes.py, Created by Janrey "CodexLink" Licas
# ! A set of attributes to pass on Entrpoint's Constructor to Instantiate Discord Bot and other Subclasses.
# * Seperated for Code Clarity and Focused Environment specifically for Entrypoint.

from collections import namedtuple
from discord import Activity, Intents, CustomActivity, PartialEmoji
from .constants import RP_ATTRS_DEFAULT
from datetime import datetime as dt

"""
# Bot's Intents

* I'm not gonna use default()'s intents. But rather, have to declare them
* on my own. This was done to properly include 'only' important features of the bot.
"""

attr_intents = Intents.none()

attr_intents.bans = True  # Has the right to ban people from manipulating the bot.
attr_intents.emojis = False  # Has no access to emojis for reacts in general.
attr_intents.invites = True  # Disallow people from inviting this bot because it doesn't make any difference.
attr_intents.messages = False  # Has no access to messages for reacts in general.
attr_intents.presences = True  # Has access to presence for presence record to Firebase.
attr_intents.dm_messages = True  # Has access to Direct Message, specifically.
attr_intents.dm_reactions = (
    True  # Has access to Direct Message Reactions, specifically.
)

"""
# Bot's Presence Activity

* All Possible Configurations were Added.
! But not all of them will be displayed since it was a bot who uses it.
* The following elements were useful:
1. RP_APP_ID — Application ID
2. RP_NAME — Application Name
3. RP_TYPE — Activity Type

"""

ATTR_ACTIVITY = Activity(
    application_id=RP_ATTRS_DEFAULT["RP_APP_ID"],
    name=RP_ATTRS_DEFAULT["RP_NAME"],
    type=RP_ATTRS_DEFAULT["RP_TYPE"],
    state=RP_ATTRS_DEFAULT["RP_STATE"],
    details=RP_ATTRS_DEFAULT["RP_DETAILS"],
    assets={
        "large_image": RP_ATTRS_DEFAULT["RP_ASSETS"]["ASSET_LARGE_IMAGE"],
        "large_text": RP_ATTRS_DEFAULT["RP_ASSETS"]["ASSET_LARGE_TEXT"],
        "small_image": RP_ATTRS_DEFAULT["RP_ASSETS"]["ASSET_SMALL_IMAGE"],
        "small_text": RP_ATTRS_DEFAULT["RP_ASSETS"]["ASSET_SMALL_TEXT"],
    },
    # emoji,
    start=dt.now(),
    large_image_text=RP_ATTRS_DEFAULT["RP_IMAGE_TEXTS"]["LARGE_IMAGE_TEXT"],
    small_image_text=RP_ATTRS_DEFAULT["RP_IMAGE_TEXTS"]["SMALL_IMAGE_TEXT"],
)


# # Attribute Entrypoint
print("Attribute > ", __name__)

if __name__ == "__main__":
    raise SystemExit(
        "You cannot run this attribute module directly! Please run the src/entrypoint.py instead!"
    )
