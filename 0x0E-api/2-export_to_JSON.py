#!/usr/bin/python3
"""module 2-export_to_JSON.py"""
import json
import requests
import sys


def export_to_json():
    """exports API data into JSON format"""
    user_id = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users{}'.format(url, user_id)

    username = requests.get(users_url).json().get('username')
    employee_todo = requests.get('{}/todos?userID={}'.format(url, user_id)).json()

    employee_dict = {}
    tasks_list = []

    for task in employee_todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks_list.append(task_dict)
    employee_dict[user_id] = tasks_list
    with open('{}.json'.format(user_id), "w") as JSONFile:
        json.dump(dict, JSONFile)


if __name__ == "__main__":
    export_to_json(argv[1])
