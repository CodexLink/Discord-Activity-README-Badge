#
# # utils/workflow_entrypoint.py, Created by Janrey "CodexLink" Licas
# ! A Bot's Workflow of Entrypoint. Containerized for Remote Host.

# * PEP 8 and 484 Compliant.

import inspect
from ast import literal_eval
from os import listdir, system # Might use subprocess on system.
from subprocess import Popen as run_command, run
from os.path import isfile, join
from sys import argv
import discord
from discord import Activity, CustomActivity
from discord import activity
from discord.ext import commands

from private import DISCORD_CRENDENTIALS
from typing import Dict, List, Tuple
from attributes.attributes import ATTR_ACTIVITY
from attributes.constants import (
    COGS_DIR_NAME,
    ON_READY_MESSAGE,
    PREFIX_COMMAND,
)


class ProfileMDBot(commands.Bot):
    def __init__(self, **kwargs: Dict[str, Tuple[object, object]]) -> None:
        try:
            self.presence_activity = kwargs["PRESENCE_ACTIVITY"]

            super().__init__(command_prefix=kwargs["PREFIX_COMMAND"], activity=kwargs["PRESENCE_ACTIVITY"])

        except KeyError:
            pass

    async def on_ready(self) -> None:
        print(ON_READY_MESSAGE, self.user, "\n")

        print("Ready!")


if __name__ == "__main__":
    run_command("CLS", shell=True).communicate()

    success_extension_count: int = 0
    instance = ProfileMDBot(
        **{
            "PREFIX_COMMAND": PREFIX_COMMAND,
            "PRESENCE_ACTIVITY": ATTR_ACTIVITY,
        }
    )

    for eachCogs in [
        cogsExt.replace(".py", "")
        for cogsExt in listdir(COGS_DIR_NAME)
        if isfile(join(COGS_DIR_NAME, cogsExt))
    ]:
        try:
            instance.load_extension(COGS_DIR_NAME + "." + eachCogs)
            success_extension_count += 1

        except (discord.ClientException, ModuleNotFoundError) as ExtensionError:
            raise SystemExit(
                "Error Loading Extension '%s': %s" % (eachCogs, ExtensionError)
            )

    print(
        "%s %s Successfully Loaded."
        % (
            success_extension_count,
            "Extensions" if success_extension_count > 1 else "Extension",
        )
    )

    instance.run(DISCORD_CRENDENTIALS)

else:
    raise SystemError("You cannot run this entrypoint file as a module to other file!")
