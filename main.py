import discord
from discord.ext import commands
from googletrans import Translator



intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.messages = True
intents.message_content = True



client = discord.Client(intents=intents)
translator = Translator()



TOKEN = 'MTI0MzgyNjg3ODU2NTg0NzA1MA.GwcG4p.S4zj-efNnE9-ZrVHv6JklucGGSKRI5EPVvUOtc'


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!translate'):
        parts = message.content.split(' ', 2)
        if len(parts) < 3:
            await message.channel.send('Usage: !translate <language_code> <text>')
            return

        lang = parts[1]
        text = parts[2]

        try:
            translated = translator.translate(text, dest=lang)
            await message.channel.send(translated.text)
        except Exception as e:
            await message.channel.send(f'Error: {str(e)}')


client.run('MTI0MzgyNjg3ODU2NTg0NzA1MA.GwcG4p.S4zj-efNnE9-ZrVHv6JklucGGSKRI5EPVvUOtc')