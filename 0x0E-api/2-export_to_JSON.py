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
    tasks = requests.get('{}/todos?userID={}'.format(url, user_id)).json()

    dict = {}
    dict_list = []

    for task in tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        dict_list.append(task_dict)

    with open('{}.json'.format(user_id), "w") as json_file:
        dict[user_id] = dict_list
        json.dump(dict, json_file)


if __name__ == "__main__":
    export_to_json(argv[1])
