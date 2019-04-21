import discord
import asyncio
from discord import Game

token = ''
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as : ", client.user.name)
    print("ID : ", client.user.id)
@client.event
async def on_message(m):
    if m.content == "!ping":
        await client.send_message(m.channel, ":ping_pong: Pong !")

client.run(token)
