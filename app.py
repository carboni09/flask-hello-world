# from flask import Flask
# app = Flask(__name__)

# #from apscheduler.schedulers.background import BackgroundScheduler
# #from apscheduler.triggers.interval import IntervalTrigger


# #scheduler = BackgroundScheduler()
# #scheduler.start()


# def job_function():
#     print("Hello, World!")


# # scheduler.add_job(
# #     func=job_function,
# #     trigger=IntervalTrigger(seconds=15),
# #     id='my_job_id',
# #     name='Print "Hello, World!" every minute',
# #     replace_existing=True)




# # @app.before_first_request
# # def initialize():
# #     # ... other initialization code ...
# #     print('init')
# #     #scheduler.start()

# # @app.teardown_appcontext
# # def shutdown_scheduler(exception=None):
# #     scheduler.shutdown()

# @app.route('/')
# def hello_world():
#     return 'Hello, World!!!!!!'
    
# app.run(host='0.0.0.0')

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('/hello'):
    quote = get_quote()
    await message.channel.send(quote)

  

  

  

  

  

keep_alive()
client.run(os.getenv('TOKEN'))
