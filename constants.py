#
# # constants/literals.py, Created by Janrey "CodexLink" Licas
# ! A set of constants in C++ Macro Variable Definition Pattern.
# * For use both, workflow_entrypoint and bot_entrypoint.py

# # Cross Compatible Labelled Constants
# ! Exit Return Codes
EXIT_SUCCESS = 0
EXIT_FAILED = 1

# # Workflow Entrypoint Constants
ENTRYPOINT_MODES = {
    "CHECKER_CANDIDATE_ARGS": ("-C", "-CH", "--CHECKER"),
    "UPDATER_CANDIDATE_ARGS": ("-U", "-UP", "--UPDATER")
}

HELP_MESSAGE = """
    Hello.

    Available Commands:

"""

# # Bot Entrypoint Constants