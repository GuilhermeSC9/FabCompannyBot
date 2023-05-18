import discord
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'f!aluguel':
            await message.channel.send(f'{message.author.name} *Exibir tabela, listando a disposição de cada farm, quem está alugando, por quanto tempo, se foi pago ou não*')

client = MyClient(intents=intents)
client.run('MTA2MzE4OTQ2OTI3ODI1MzExNw.GsKQZ9.k_ng5-xCPQsROe8Q64kCDByU9DlLs85AJpaJw0')