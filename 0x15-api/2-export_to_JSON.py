#!/usr/bin/python3
""" 2. Export to JSON """

import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = int(sys.argv[1])

    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/\
{USER_ID}")

    tasks = {f"{USER_ID}": []}

    objects = json.loads(todo_response.text)
    user = json.loads(user_response.text)

    USER_NAME = user.get('username')

    for object in objects:
        if object.get('userId') == USER_ID:
            new_entry = {}
            new_entry['task'] = object.get('title')
            new_entry['completed'] = object.get('completed')
            new_entry['username'] = USER_NAME
            tasks[f"{USER_ID}"].append(new_entry)

    json_file_name = f"{USER_ID}.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(tasks, json_file)
