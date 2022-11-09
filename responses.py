import requests
import json
import random

def get_quote():
  response  = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" +json_data[0]['a']

  return quote

def handle_repsonse(message) -> str:
  p_message = message.lower()

  if p_message == 'hello':
    return "Hey there!"

  if p_message == 'roll':
    return str(random.randint(1, 6))

  if p_message == '!help':
    return "`Please contact support for help.`"

  if p_message == 'quote':
    return get_quote()