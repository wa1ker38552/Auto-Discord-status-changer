import requests, time, random
from alive import keepAlive

interval = 0.5 # time between each word
waittime = 2 # time it lingers on last word

status = [
  'really cool message'.split(),
  'another really cool message'.split(),
  'dumb message'.split(),
  'troll yes'.split(),
  'last message'.split()
]

headers = {
  'authorization': 'YOUR DISCORD AUTH TOKEN',
  'content-type': 'application/json'
}

keepAlive()
while True:
  message = random.choice(status)
  for char in message:
    json = {
      'custom_status': {
        'text': char, 
        'emoji_name': "👉" # whatever emoji you want
      }
    }
    r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=json)
    time.sleep(interval)
  time.sleep(waittime)
