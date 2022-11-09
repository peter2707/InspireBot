import discord
import responses
import os
from server import server

async def send_message(message, user_message, is_private):
  try:
    response = responses.handle_repsonse(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
  except Exception as e:
    print(e)

def run_discord_bot():
  intents = discord.Intents.default()
  intents.message_content = True
  token = os.environ['token']
  
  client = discord.Client(intents=intents)
  
  @client.event
  async def on_ready():
    print(f'We have logged in as {client.user}')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' on channel: {channel}")

    if user_message[0] == "?":
      user_message = user_message[1:]
      await send_message(message, user_message, is_private = True)
    else:
      await send_message(message, user_message, is_private = False)

  server()
  client.run(token)