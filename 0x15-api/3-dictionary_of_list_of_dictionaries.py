#!/usr/bin/python3
"""
3. Dictionary of list of dictionaries
"""

import json
import requests


if __name__ == "__main__":
    # Fetch user data
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Fetch task data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_response.json()

    # Prepare data structure
    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in todos if task['userId'] == user_id]

        tasks_list = []
        for task in user_tasks:
            task_dict = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            tasks_list.append(task_dict)
        data[user_id] = tasks_list

    # Export to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
