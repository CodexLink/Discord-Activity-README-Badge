from discord.ext import commands


class RegistrationPhase(commands.Cog, name="Registration Phase Commands"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.transaction = None
        self.gh_link = None
        self.gh = None

        # Add other Stateful Variables here.

    @commands.command(name="intro")
    async def introduction(self) -> bool:
        pass

    @commands.command(name="intro2")
    async def introduction_2(self, url_gh_profile: str) -> None:
        pass


def setup(bot: commands.Bot) -> None:
    if __name__ == "__main__":
        raise SystemExit(
            "You cannot run this file directly, this has to be imported to entrypoint.py!"
        )
    else:
        bot.add_cog(RegistrationPhase(bot))
