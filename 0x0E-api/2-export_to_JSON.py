#!/usr/bin/python3
"""module 2-export_to_JSON.py"""
import json
import requests
from sys import argv


def export_to_json(user_id):
    """exports API data into JSON format"""

    url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users{}'.format(url, user_id)

    username = requests.get(users_url).json().get('username')
    employee_tasks = requests.get('{}/todos?userID={}'.format(url, user_id)).json()

    dict = {}
    list_of_dicts = []

    for task in employee_tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        list_of_dicts.append(task_dict)

    with open('{}.json'.format(user_id), "w") as json_file:
        dict[user_id] = list_of_dicts
        json.dump(dict, json_file)


if __name__ == "__main__":
    export_to_json(argv[1])
