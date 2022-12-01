#!/usr/bin/python3
"""module 0-gather_data_from_an_API
Python script that, using this REST API, 
for a given employee ID, returns information 
about his/her TODO list progress.
"""
import requests
from sys import argv


def get_employee_todo():
    """returns information about employee TODO list progress"""

    data = {'Id': id}
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + 'users', params={'id': id}).json()
    name = users[0]['name']
    todos = requests.get(url + 'todos', params={'userId': id}).json()
    return ([name, todos])

def show_employee_todo():
    """shows information about employee TODO list progress"""
    name = data[0]
    todo = data[1]
    n = 0
    print_string = ""
    for task in todo:
        if task['completed'] is True:
            n += 1
            print_string += '\t ' + task['title'] + '\n'
    print('Employee {} is done with task({}/{}):'.format(name, n, len(todo)))
    print(print_string, end='')


if __name__ == '__main__':
    data = get_employee_todo(argv[1])
    show_employee_todo(data)
