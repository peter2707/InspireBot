import discord
import responses
import os

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
    print('We have logged in as {0.user}'.format(client))

  client.run(token)