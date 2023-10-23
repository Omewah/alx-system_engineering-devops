#!/usr/bin/python3
'''A script that gathers data from REST API and exports to JSON format.
'''
import json
import requests


API_URL = 'https://jsonplaceholder.typicode.com'
'''The REST API's URL to gather employee information from.'''


if __name__ == '__main__':
    user_ID = requests.get('{}/users'.format(API_URL)).json()
    todo_ID = requests.get('{}/todos'.format(API_URL)).json()
    data_export = {}
    for user in user_ID:
        id = user.get('id')
        user_name = user.get('username')
        todo_list = list(filter(lambda x: x.get('userId') == id, todo_ID))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todo_list
        ))
        data_export['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data_export, file)
