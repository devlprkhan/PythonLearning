'''
Exercise#10

Use the NewsAPI and the requests module to fetch the daily news related to 
different topics. Go to: https://newsapi.org/ and explore the various options 
to build you application
'''

import requests as req
import json
api_key = "f4b2cc6a95b947299dc186fe0d6c8c44"

def beautify_response(data):
  json_object = json.loads(data)
  json_formatted_str = json.dumps(json_object, indent=2)
  return json_formatted_str

def get_news(topic):
  crafted_url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
  response = req.get(crafted_url)
  return beautify_response(response.text)

topic = input(f"Please enter the topic you want to search for: ")
if not len(topic) == 0:
  res = get_news(topic)
  print("Topic: ", res)
else:
  raise ValueError("Please enter valid topic!")
