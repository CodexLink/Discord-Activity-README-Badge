#
# # utils/handler_attributes.py, Created by Janrey "CodexLink" Licas
# ! A set of attributes to pass on Discord's Client or Bot's Parameter.
# * Seperated for Code Clarity and Focused Environment

"""
! The reason why attributes for handlers which are Bot and Client Class Instances are
shared because certain instantiation requires synced attributes. Meaning I may be unable
to fetch for activities in Client's Side while it was enabled in Bot's Side.
"""

from discord import Intents
"""
I'm not gonna use default()'s intents. But rather, have to declare them
on my own. This was done so that it would make it clear for me when I get
back to these intents when a particular problem overcomes.
"""

handler_intents = Intents.none()

handler_intents.bans = True
handler_intents.emojis = True
handler_intents.presences = True
handler_intents.invites = True  # For telling that inviting this bot is not allowed.
handler_intents.dm_messages = True
handler_intents.dm_reactions = True

from discord import BaseActivity, CustomActivity

# handler_activity =


if __name__ != "handler_attributes":
    raise SystemExit(
        "You cannot run this module directly! Please run discord_client_handler.py!"
    )
