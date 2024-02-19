#!/usr/bin/python3
"""Exports given to-do list information for specified employee ID to CSV format,"""

import csv
import requests
import sys


if __name__ == "__main__":
    # Get user ID from command-line arguments provided to script,
    user_id = sys.argv[1]

    # Define base URL for JSON API,
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from API,
    # convert response to a JSON object,
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract username from user data,
    username = user.get("username")

    # Fetch to-do list items associated with,
    # given user ID and convert response to a JSON object,
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Use a list comprehension to iterate over the to-do list items,
    # Write each item's details (user ID, username, completion status,
    # and title) as a row in the CSV file,
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

