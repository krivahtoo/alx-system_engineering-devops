#!/usr/bin/python3
"""
2. Export to JSON
"""

import json
import requests
import sys


def employee_todo_progress(employee_id):
    """
    export data in the JSON format.
    """
    # Base URL for JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    employee_name = user_data['username']

    # Fetch employee TODO list data
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}.")
        return

    todos = todos_response.json()

    # Calculate the number of completed tasks and the total number of tasks
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with\
 tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

    # Prepare data for JSON export
    tasks_data = [{
        "task": todo['title'],
        "completed": todo['completed'],
        "username": employee_name
    } for todo in todos]

    json_data = {str(employee_id): tasks_data}

    # Export data to JSON
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, mode='w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_todo_progress(employee_id)
