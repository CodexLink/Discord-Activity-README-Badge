from discord.ext import commands
from datetime import datetime

class UserStatuses(commands.Cog, name="User Status Report Commands"):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.user_stats = None

    # Require confirmation.
    @commands.command(name="")
    async def reset_last_saved_data(self, response: bool) -> bool:
        pass

    # Might use embed for badge display here.
    @commands.command(name="")
    async def show_saved_data(self) -> None:
        pass

    # ! Only allow one condition allowed.
    @commands.command(name="")
    async def save_data_on_condition(self, conditions: str) -> bool:
        pass


def setup(bot: commands.Bot) -> None:
    if __name__ == "__main__":
        raise SystemExit(
            "This file cannot be directly used. It has to be imported in entrypoint.py!"
        )
    else:
        bot.add_cog(UserStatuses(bot))