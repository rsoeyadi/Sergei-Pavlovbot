import os
from openai import OpenAI
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())
openai_client = OpenAI(
  api_key = os.environ.get("OPENAI_API_KEY"),
)

# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(f'{client.user} has connected to {guild.name}')
#     channel = discord.utils.get(guild.text_channels, name='general')
#     msgs = [msg async for msg in channel.history(limit=5, oldest_first=False)]
  
@client.event
async def on_message(msg):
    if msg.author == client.user: # don't respond to the bot's own messages
        return
    
    guild = discord.utils.get(client.guilds, name=GUILD)
    channel = discord.utils.get(guild.text_channels, name='general')
    completion = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": os.getenv('CHATGPT_CONTENT')},
        {
            "role": "user",
            "content": msg.content
        }
        ]
    )

    content = completion.choices[0].message.content
    
    if channel:
        await channel.send(
            content
        )
     
@client.event
async def on_member_join(member):
    channel = client.channels.get('general')
    if channel:
        await channel.send(
            f'{member.name}, do you want that thing to go from coast to coast? Or is it fine the way it is, being Dijkstra?'
        )

client.run(TOKEN)

