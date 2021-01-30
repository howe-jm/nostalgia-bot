import os
import discord
import aiohttp
import requests
import json

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

def get_doge():
    response = requests.get("https://dog.ceo/api/breed/corgi/images/random")
    json_date = json.loads(response.message)
    doge = json_data['message']
    return (doge)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('ANGULAR'):
    await message.channel.send('REACT!!!!!!')

  elif message.content.lower().startswith('angular'):
    await message.channel.send('React!')

  elif message.content.startswith('REACT'):
    await message.channel.send('ANGULAR!!!!!')

  elif message.content.lower().startswith('react'):
    await message.channel.send('Angular!')

  if message.content.startswith('<:doge:751831415594680410>'):
    doge = get_doge()
    async with aiohttp.ClientSession() as session:
        async with sesson.get(doge) as resp:
            if resp.status != 200:
                return await channel.send('Could not download file')
            data = io.BytesIO(await resp.read())
            await channel.send(file=discord.File(data, 'doge.png'))
    

client.run(TOKEN)