import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to {guild.name}')
    channel = discord.utils.get(guild.text_channels, name='general')
    msgs = [msg async for msg in channel.history(limit=5, oldest_first=False)]
    for msg in msgs:
        print(msg.content, sep="\n")
        
@client.event
async def on_member_join(member):
    channel = discord.utils.get(guild.text_channels, name='general')
    if channel:
        await channel.send(
            f'{member.name}, do you want that thing to go from coast to coast? Or is it fine the way it is, being Dijkstra?'
        )

client.run(TOKEN)

