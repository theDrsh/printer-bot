import secrets
import discord
import time
import yaml

BOT = discord.Client()

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
        self.events = OctoprintEvents()

@BOT.event
async def on_ready(self):
    pb = PrinterBot()
    while(1):
        time.sleep(1)
        pb.events.update()

@BOT.event
async def on_message(self, message):
    if message.channel.name in secrets.allowed_channels:
        print('Message from {0.author}: {0.content}'.format(message))

if __name__ == "__main__":
    BOT.run(secrets.bot_token)
