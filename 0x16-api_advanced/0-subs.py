#!/usr/bin/bash/python3

"""
A module queries Reddit API and returns no. of subscribers
(not active users, total subscribers) for a given subreddit
If an invalid subreddit is given, function should return 0,
"""

import requests

def number_of_subscribers(subreddit):
    """Returns all  subscribers of the sub reddit,"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0"}
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 404 or response.status_code == 302:
        return 0
    return response.json().get("data").get("subscribers")

