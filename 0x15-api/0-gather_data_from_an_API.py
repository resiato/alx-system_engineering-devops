#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    employeeName = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_no_of_tasks = 0
    no_of_done_tasks = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            total_no_of_tasks += 1
            if task.get('completed'):
                no_of_done_tasks += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employeeName, no_of_done_tasks, total_no_of_tasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
