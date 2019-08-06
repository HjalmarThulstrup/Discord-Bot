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

client.run("NTY0MTA1MzM2MjI3ODg5MTUz.XUmC4w.iCyZgqmP_aDuCxZsjRp6I0WJPhU")