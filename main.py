import os
import io
import discord
import aiohttp
import requests
import json

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = discord.Client()


def get_doge():
    response = requests.get("https://dog.ceo/api/breed/shiba/images/random")
    json_data = json.loads(response.text)
    doge = json_data["message"]
    return doge


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("cat"):
        await message.channel.send("Puppies")

    if message.content.startswith("ANGULAR"):
        await message.channel.send("REACT!!!!!!")

    elif message.content.lower().startswith("angular"):
        await message.channel.send("React!")

    if message.content.startswith("REACT"):
        await message.channel.send("ANGULAR!!!!!")

    elif message.content.lower().startswith("react"):
        await message.channel.send("Angular!")

    if "asm" in message.content.lower().split():
        await message.channel.send(
            "Are you trying to reach your ASM? You will find their email address somewhere around here. Otherwise, please reach out to Metty, who is the ASM now, and we’ll be happy to support."
        )
        
    if "im such a failure and idk what to do with my life" in message.content.lower().split():
        await message.channel.send(
            "NO, you are fucking AMAZING, you are litteraly made out of iron from heart of a dying star, out of 7+ billion people you are alive, healthy and have the world of options open to you, and lastly did I mention that you FUCKING ROCK. NOW TO UNFUCK YOURSELF AND SMILE GOOD DAMMIT."
        )

    if message.content.startswith("<:doge:751831415594680410>"):
        doge = get_doge()
        async with aiohttp.ClientSession() as session:
            async with session.get(doge) as resp:
                if resp.status != 200:
                    return await channel.send("Could not download file")
                data = io.BytesIO(await resp.read())
                await message.channel.send(file=discord.File(data, "doge.png"))


client.run(TOKEN)
