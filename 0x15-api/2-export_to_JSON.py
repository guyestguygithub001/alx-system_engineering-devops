#!/usr/bin/python3
"""
Exports to-do list info. for a given employee ID to JSON format,

This script takes an employee ID as a command-line argument and exports
corresponding user info. and to-do list to JSON file,
"""

import requests
import json
import sys


if __name__ == "__main__":
    # fetches employee ID from command-line argument,
    user_id = sys.argv[1]

    # Base URL for JSONPlaceholder API,
    url = "https://jsonplaceholder.typicode.com/"

    # Fetches user information using provided employee ID,
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the to-do list for the employee using provided employee ID.
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Creates python dictionary containing user and to-do list info.
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Write data to a JSON file with employee ID as filename.
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

