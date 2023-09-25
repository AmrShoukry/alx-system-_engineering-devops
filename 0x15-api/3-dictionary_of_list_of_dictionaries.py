#!/usr/bin/python3
""" 3. Dictionary of list of dictionaries """

import json
import requests
import sys

if __name__ == '__main__':
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/")

    tasks = {}

    objects = json.loads(todo_response.text)
    users = json.loads(user_response.text)

    for object in objects:
        user_id = object.get('userId')
        if tasks.get(f"{user_id}") is None:
            tasks[f"{user_id}"] = []

        new_entry = {}
        new_entry['task'] = object.get('title')
        new_entry['completed'] = object.get('completed')
        new_entry['username'] = users[user_id - 1].get('username')
        tasks[f"{user_id}"].append(new_entry)

    json_file_name = "todo_all_employees.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(tasks, json_file)
