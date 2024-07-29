#!/usr/bin/python3
"""
0. Gather data from an API
"""

import requests
import sys


def employee_todo_progress(employee_id):
    """
    script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
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
    employee_name = user_data['name']

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
