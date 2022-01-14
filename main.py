import os
my_secret = os.environ['TOKEN']
api_cat_key = os.environ['CAT_API_KEY']

# importing discord library : async in nature
import discord
import requests
import json
from keepAlive import keepAlive

# getting qoutes funtion
def get_qoute():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  qoute = json_data[0]['q'] + " -by " + json_data[0]["a"]
  return(qoute)

# getting cat images function
def get_cat():
  url = "https://api.thecatapi.com/v1/images/search"
  headers = {'x-api-key': api_cat_key}
  response = requests.request("GET", url, headers=headers)
  json_cat_data = json.loads(response.text)
  cat = json_cat_data[0]["url"]
  return(cat)


# getting jokes api key
def get_joke():
  url = 'https://api.jokes.one/jod?category=knock-knock'
  api_token = "YOUR API KEY HERE"
  headers = {'content-type': 'application/json',
	   'X-JokesOne-Api-Secret': format(api_token)}

  response = requests.get(url, headers=headers)
  #print(response)
  #print(response.text)
  jokes=response.json()['contents']['jokes'][0]
  print(jokes)
  

# client use events: funtion names are from discord.py library, bot looks for these names to do things;
client  = discord.Client()

# creating events
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$help'):
    await message.channel.send("things I can do: 1) use '$inspire' to get qoutes! 2) use '$cat' to get cat images! ")

  if message.content.startswith('$inspire'):
    qoute = get_qoute()
    await message.channel.send(qoute)
  
  if message.content.startswith('$cat'):
    cat = get_cat()
    await message.channel.send(cat)
  


keepAlive()
# to run the bot
client.run(my_secret)


