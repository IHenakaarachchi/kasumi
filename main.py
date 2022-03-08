import discord
import os
import io
import json
import requests

TOKEN=os.getenv("TOKEN")
client=discord.Client()
embed=discord.Embed()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  username=str(message.author).split('#')[0]
  usr_msg=str(message.content)
  channel=str(message.channel.name)
  print(f'{username}:{usr_msg} ({channel})')

  if message.author==client.user:
    return

  if usr_msg.lower()=="-k hello":
    await message.channel.send(f"Hi! I'm Kasumi\n howdy? @{username}")
    return

  elif usr_msg.lower()=="-k hru":
    await message.channel.send("I'm doing great! How are you?")
    return

  elif ('sniperwolf' or 'sssniperwolf') in message.content.lower():
    embed.set_image(url='https://tenor.com/view/sssniperwolf-gif-18432997')
    await message.channel.send(embed=embed)
    return
	
  elif 'happy birthday' in message.content.lower():
    embed.set_image(url='https://tenor.com/SZbC.gif')
    await message.channel.send(embed=embed)
    return
	
client.run(TOKEN)
