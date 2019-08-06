import discord, random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        msg_str = str(message.content)
        if str(message.author) == "spanky#3159":
            if "trash" in msg_str.lower() or "t r a s h" in msg_str.lower():
                spankId = "<@259430446037860353>"
                await message.channel.send(msg_str.replace("trash", "amazing, %s loves it!" % spankId))

client = MyClient()

client.run("NjA4MjY5NDc2OTM2NTQ4MzYy.XUmFxA.B3gNRdB3is1gAgUPGprq6vYpB78")