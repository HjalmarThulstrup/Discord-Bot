import discord, random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        num = random.randint(1,11)
        if num == 7:
            await message.channel.send("you're a dink")

client = MyClient()

client.run("NjA4MjY5NDc2OTM2NTQ4MzYy.XUltJw.BTOXhom_fg-vcyxQN3NzN5705jY")