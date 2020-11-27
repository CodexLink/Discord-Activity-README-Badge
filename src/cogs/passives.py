from discord.ext import commands
from discord import Activity, ActivityType, CustomActivity, PartialEmoji
from datetime import datetime


# is_owner is experimental and untested! Check before committing.
class SpecialPassives(commands.Cog, command_attrs=dict(hidden=True, is_owner=True), name="Special Passives for Debugs"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="Bot Reset on Runtime")
    async def reset_bot(self, credentials: str) -> bool:
        pass

    @commands.command(name="Set Custom Status")
    async def set_custom_status(self, emoji: PartialEmoji, status: str) -> bool:
        pass

    @commands.command(name="Set User Check Time")
    async def set_check_time(self, base_dt: datetime, interval_hr: int) -> bool:
        pass

    @commands.command(name="Set Presence Status")
    # more validation on ctx soon.
    async def set_presence_status(self, ctx: dict, apply_now: bool) -> bool:
        pass

    @commands.command(name="Set Internal Logging")
    async def set_type_logging(self, type: str, literal: bool) -> bool:
        pass

    @commands.command(name="Include / Exclude Type Logging")
    # Certain types may have a subset of log_names to another type. Be careful.
    async def include_type_logging(
        self, type: str, log_name: str, enable: bool, immediate: bool
    ) -> bool:
        pass

    @commands.command(name="Set User Ban State")
    # clarification on use of disc_id type is not viable. Check for other class soon.
    # Gonna create ban_type soon.
    async def set_user_ban_state(
        self, disc_id: str, ban_type: bool, reason: str
    ) -> None:
        pass

    @commands.command(name="Set Bot Mode")
    # A set of Modes here.
    async def set_bot_mode(self, proposed: str) -> bool:
        pass

def setup(bot: commands.Bot) -> None:
    if __name__ == "__main__":
        raise SystemExit(
            "This file cannot be directly used. It has to be imported in entrypoint.py!"
        )
    else:
        bot.add_cog(SpecialPassives(bot))