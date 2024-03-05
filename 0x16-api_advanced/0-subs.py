#!/usr/bin/python3

"""
Script to query subscribers on a given Reddit subreddit,
"""

import requests


def number_of_subscribers(subreddit):
    """Returns total no. of subscribers in given subreddit,"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0i
