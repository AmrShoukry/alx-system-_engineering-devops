#!/usr/bin/python3
""" 1. Export to CSV """

import csv
import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = int(sys.argv[1])

    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/\
{USER_ID}")

    completed_titles = []

    objects = json.loads(todo_response.text)
    user = json.loads(user_response.text)

    USER_NAME = user.get('username')

    for object in objects:
        if object.get('userId') == USER_ID:
            new_entry = []
            new_entry.append(USER_ID)
            new_entry.append(USER_NAME)
            new_entry.append(object.get('completed'))
            new_entry.append(object.get('title'))
            completed_titles.append(new_entry)

    csv_file_name = f"{USER_ID}.csv"

    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(completed_titles)
