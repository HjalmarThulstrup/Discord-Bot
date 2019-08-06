import discord, random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        msg_str = str(message.content)
        if str(message.author) == "spanky#3159":
            if "trash" in msg_str.lower():
                await message.channel.send(msg_str.replace("trash", "amazing, @spanky#3159 loves it!"))

client = MyClient()

client.run("NjA4MjY5NDc2OTM2NTQ4MzYy.XUltJw.BTOXhom_fg-vcyxQN3NzN5705jY")