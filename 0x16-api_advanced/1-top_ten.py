#!/usr/bin/python3

"""
A script that prints hotposts on a Reddit Subreddit,
"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit,

    Args:
        subreddit (str): The name of the subreddit to query,
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "YourAppName/0.1"}  # Replace with your app name
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data.get("data", {}).get("children", []):
            if len(post) < 10:  # Check if post data exists
                continue
            title = post["data"].get("title", "")
            print(title)
            if len(data.get("data", {}).get("children", [])) == 10:
                break  # Stop after printing 10 titles
    else:
        print(None)

