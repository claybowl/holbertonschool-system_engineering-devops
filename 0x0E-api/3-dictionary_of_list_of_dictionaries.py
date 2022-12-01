#!/usr/bin/python3
"""module 3-dictionary_of_list_of_dictionaries
extend module 0 Python script to export
data in the JSON format.
"""
import json
import requests
import sys


def everyone_todo_to_JSON():
    """method creates dictionary list of dictionaries"""
    url = "https://jsonplaceholder.typicode.com/"

    employee_names = requests.get(url + 'users').json()
    employees_todos = requests.get(url + 'todos').json()

    return_dict = {}
    all_users_dict = {}

    for employee in employee_names:
        user_id = employee.get('id')
        return_dict[user_id] = []
        all_users_dict[user_id] = employee.get('username')
    # print(all_users_dict)
    for task in employees_todos:
        employee_tasks_dict = {}
        user_id = task.get('userId')
        employee_tasks_dict['username'] = all_users_dict.get(user_id)
        employee_tasks_dict['task'] = task.get('title')
        employee_tasks_dict['completed'] = task.get('completed')
        return_dict.get(user_id).append(employee_tasks_dict)

    with open('todo_all_employees.json', 'w') as JSONFile:
        json.dump(return_dict, JSONFile)


if __name__ == "__main__":
    everyone_todo_to_JSON()
