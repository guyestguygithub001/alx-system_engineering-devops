#!/usr/bin/python3
"""
A script that is to  print hot posts on a given Reddit subreddit
"""

import requests


def top_ten(subreddit):
    """Prints titles of 10 hottest posts on given subreddit,"""
    # Constructs URL for subreddit's hot posts in JSON format,
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Defines headers for HTTP request, including User-Agent,
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Defines parameters for request, limits no. of posts to 10
    params = {
        "limit": 10
    }

    # Sends GET request to subreddit's hot posts page,
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Checks if response status code read a not-found error (404),
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response, extracts data section,
    results = response.json().get("data")

    # Prints titles of top 10 hottest posts,
    [print(c.get("data").get("title")) for c in results.get("children")]

