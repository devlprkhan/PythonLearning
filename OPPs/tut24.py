'''
Requests module in python

The Python Requests module is an HTTP library that enables developers to send
HTTP requests in Python. This module enables you to send HTTP requests using
Python code and makes it possible to interact with APIs and web services.
'''

import requests
from bs4 import BeautifulSoup

# Get
# url = "https://chat.openai.com/"
# response = requests.get(url)

# print(response.text)

# Post
body = {
    "title": 'Hello',
    "body": 'in return',
    "userId": 1,
  }

headers = {
  "Content-type": 'application/json; charset=UTF-8',
}

# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.post(url, headers=headers, json=body)
# print(response.text)

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# Beautiful Soup
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h1"):
  print(heading.text)