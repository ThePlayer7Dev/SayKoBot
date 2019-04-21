import discord
import asyncio
from discord import Game

token = 'NTY5NTEzNjMyNzQ5MTkxMTg0.XLxvCQ.GegPJB0Zzq-iBwg51HjsF9OqCcI'
client = discord.Client()

@client.event
async def on_ready():
    print("Login in as : ", client.user.name)
    print("ID : ", client.user.id)
@client.event
async def on_message(m):
    if m.content.startswith == "ok":
        await client.send_message(m.channel, "not")

client.run(token)
