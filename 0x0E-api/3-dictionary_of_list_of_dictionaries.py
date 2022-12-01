#!/usr/bin/python3
"""module 3-dictionary_of_list_of_dictionaries
extend module 0 Python script to export
data in the JSON format.
"""
import json
import requests
import sys


def todo_all_employees():
    """makes dictionary list of dictionaries"""
    url = 'https://jsonplaceholder.typicode.com'

    users = requests.get("{}/users".format(url)).json()
    todo = requests.get("{}/todos".format(url)).json()

    dict = {}
    user_dict = {}

    for user in users:
        user_id = user.get('id')
        dict[user_id] = []
        user_dict[user_id] = user.get('username')

    for task in todo:
        task_dict_emp = {}
        user_id = task.get('userId')
        task_dict_emp["username"] = user_dict.get(user_id)
        dict.get(user_id).append(task_dict_emp)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(dict, json_file)


if __name__ == "__main__":
    todo_all_employees()
