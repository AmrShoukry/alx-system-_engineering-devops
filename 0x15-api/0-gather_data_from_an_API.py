#!/usr/bin/python3
# 0. Gather data from an API
""" 0. Gather data from an API """

import requests
import sys
import json

USER_ID = int(sys.argv[1])

todos_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/\
{USER_ID}")

completed = 0
all = 0
completed_titles = []

objects = json.loads(todos_response.text)
user = json.loads(user_response.text)

for object in objects:
    if object['userId'] == USER_ID:
        all += 1
        if object['completed'] is True:
            completed += 1
            completed_titles.append(object['title'])

print(f"Employee {user['name']} is done with tasks({completed}/{all}):")

for title in completed_titles:
    print(f"\t {title}")
