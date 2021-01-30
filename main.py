import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

def get_doge():
    response = requests.get("https://dog.ceo/api/breed/corgi/images/random")
    json_date = json.loads(response.message)
    doge = json_data['message']
    return(doge)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  print(message.content)

  if message.content.startswith('ANGULAR'):
    await message.channel.send('REACT!!!!!!')

  elif message.content.lower().startswith('angular'):
    await message.channel.send('React!')

  elif message.content.startswith('REACT'):
    await message.channel.send('ANGULAR!!!!!')

  elif message.content.lower().startswith('react'):
    await message.channel.send('Angular!')

  if message.content.startswith(':doge:'):
    await channel.send(file=discord.File(fp, doge))
    

client.run(TOKEN)