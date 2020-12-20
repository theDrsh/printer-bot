import secrets
import discord
import time
import yaml



class DiscordBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.channel.name in secrets.allowed_channels:
            print('Message from {0.author}: {0.content}'.format(message))
    
class OctoprintEvents():
    def __init__(self):
        self.event_log_path = secrets.event_log
    def update(self):
        with open(self.event_log_path, "r") as event_log:
            for line in event_log.readlines():
                print(line)
        with open(self.event_log_path, "w") as event_log:
            event_log.write("")


class PrinterBot():
    def __init__(self):
        self.bot = DiscordBot()
        self.bot.run(secrets.bot_token)
        self.events = OctoprintEvents()
    

if __name__ == "__main__":
    pbot = PrinterBot()
    while(1):
        pbot.events.update()
        time.sleep(1)