import discord
README_LOCATION = "README.md"

EXIT_FAILURE = 1
EXIT_SUCCESS = 0

class MyClient(discord.Client):
    #def __init__(self, **kwargs):
    #    pass
        #if not kwargs:
        #    print("")
        #    raise SystemExit("Error: Cannot Run Process with Few Arguments Missing.")

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('.X40TWg.MfsCEjMzaeYO7etqaqXlZ2YkqQI')
