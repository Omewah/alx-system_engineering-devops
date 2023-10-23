#!/usr/bin/python3
'''A script that gathers data from REST API and exports to JSON format.'''
import json
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
            user_name = user_ID.get('username')
            todo_list = list(filter(lambda x: x.get('userId') == id, todo_ID))
            with open('{}.json'.format(id), 'w') as file:
                user_data = list(map(
                    lambda x: {
                        'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': user_name
                    },
                    todo_list
                ))
                data_export = {
                    '{}'.format(id): user_data
                }
                json.dump(data_export, file)
