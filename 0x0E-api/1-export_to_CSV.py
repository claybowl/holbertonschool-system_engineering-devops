#!/usr/bin/python3
"""module 1-export_to_CSV
extends Python script from task 0
to export data in the CSV format
"""
import csv
import requests
import sys


def export_to_CSV():
    """script reads data from API and converts and stores information in csv file"""
    num = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    url_tasks = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(num))
    tasks = requests.get(url_tasks).json()
    user_info = requests.get(url_user).json()
    employee_name = user_info.get("username")
    with open('{}.csv'.format(num), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([task.get('username'), employee_name,
                             task.get('completed'), task.get('title')])


if __name__ == '__main__':
    export_to_CSV()
