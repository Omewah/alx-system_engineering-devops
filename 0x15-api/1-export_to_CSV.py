#!/usr/bin/python3
'''A script that gathers data from REST API and exports to CSV format'''
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
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todo_list:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
