#!/usr/bin/python3
""" 0. Gather data from an API """

import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = int(sys.argv[1])

    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/\
{USER_ID}")

    complete = 0
    all = 0
    completed_titles = []

    objects = json.loads(todo_response.text)
    user = json.loads(user_response.text)

    for object in objects:
        if object.get('userId') == USER_ID:
            all += 1
            if object.get('completed') is True:
                complete += 1
                completed_titles.append(object['title'])

    print(f"Employee {user.get('name')} is done with tasks({complete}/{all}):")

    for title in completed_titles:
        print(f"\t {title}")
