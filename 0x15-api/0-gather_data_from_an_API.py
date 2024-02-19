#!/usr/bin/python3
"""
Returns given to-do list information for an employee ID,

This script takes a given employee ID as a command-line argument which fetches
a corresponding user info and to-do list from JSONPlaceholder API.
It then prints all tasks completed by given employee.
"""
import requests
import sys


if __name__ == "__main__":
    # Base URL for JSONPlaceholder API.
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee information using provided employee ID.
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get given to-do list for employee using provided employee ID.
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter completed tasks with a count.
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Prints employee's name and  number of completed tasks.
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Prints completed tasks each with indentation.
    [print("\t {}".format(complete)) for complete in completed]

