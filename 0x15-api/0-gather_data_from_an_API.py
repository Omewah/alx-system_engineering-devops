#!/usr/bin/python3
'''A script that gathers information from REST API.'''
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The REST API's URL to gather employee information from.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_ID = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todo_ID = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_ID.get('name')
            todo_list = list(filter(lambda x: x.get('userId') == id, todo_ID))
            todos_done = list(filter(lambda x: x.get('completed'), todo_list))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todo_list)
                )
            )
            for task_done in todos_done:
                print('\t {}'.format(task_done.get('title')))
