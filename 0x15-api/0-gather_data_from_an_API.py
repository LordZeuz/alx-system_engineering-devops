#!/usr/bin/python3

'''Using this REST API, for a given employee ID, returns information about
his/her TODO list progress
API: https://jsonplaceholder.typicode.com/todos?userId=2&_expand=user
prints the todos associated with user
'''

import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       '&_expand=user'.format(u_id))
    res = res.json()
    name = res[0].get('user').get('name')
    complete = [task.get('title') for task in res if task.get('completed')
                is True]
    print('Employee {} is done with tasks({}/{}):'.format(name, len(complete),
          len(res)))
    for task in complete:
        print('\t {}'.format(task))
