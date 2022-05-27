from threading import Thread
from alive import keepAlive
import requests
import random
import time
import os


def create_thread(content, emoji, token, interval=5):
  global requests_sent
  headers = {
  'authorization': token,
  'content-type': 'application/json',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
  }
  while True:
    message = random.choice(content)
    data = {'custom_status': {'text': message, 'emoji_name': emoji}}
    request = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=data)
    requests_sent += 1
    if request.status_code != 200: 
      time.sleep(5)
    else: time.sleep(interval)

if __name__ == '__main__':
  requests_sent = 0
  keepAlive()
  
  message_object = open('status_objects.txt', 'r').read().split('\n\n')
  for message_obj in message_object:
    o = message_obj.split('\n')
    Thread(target=lambda: create_thread(o[:-2], o[len(o)-2], o[len(o)-1])).start()

  print('>> Finished setting threads!')
  while True:
    os.system('clear')
    print(f'>> Requests sent: {requests_sent}')
    time.sleep(4)
