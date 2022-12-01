#!/usr/bin/python3
"""module 2-export_to_JSON.py"""
import json
import requests
import sys


def employee_todo_to_JSON():
    """This method gathers employee to do information from an API
    Employee task information is sent to a JSON file
    """
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    username = requests.get(url + 'users/{}'.format(user_id))
    employee_todo = requests.get(url + 'todos?userId={}'.format(user_id))

    username = username.json()
    employee_todo = employee_todo.json()

    employee_tasks = []

    for task in employee_todo:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = username.get('username')
        employee_tasks.append(task_dict)
    json_dict = {}
    json_dict[user_id] = employee_tasks
    with open('{}.json'.format(user_id), 'w') as JSONFile:
        json.dump(json_dict, JSONFile)


if __name__ == "__main__":
    employee_todo_to_JSON()
