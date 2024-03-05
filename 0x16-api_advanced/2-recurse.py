#!/usr/bin/python3
"""
A Script that querries list of all hot posts on a given Reddit subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves list of titles of all hot posts
    on given subreddit

    Args:
        subreddit (str): Name of subreddit
        hot_list (list, optional): List to store post titles
                                    Default is an empty list
        after (str, optional): Token used for pagination
                                Default is an empty string
        count (int, optional): Current count of retrieved posts Default is 0

    Returns:
        list: list of post titles from hot section of subreddit,
    """
    # Constructs URL for subreddit's hot posts in JSON format,
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Defines headers for HTTP request, including User-Agent,
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Defines parameters for request, including pagination and limit,
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Sends GET request to subreddit's hot posts page,
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Checks if response status code indicates not-found error (404),
    if response.status_code == 404:
        return None
    # Parse JSON response and extract relevant data,
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Appends post titles to hot_list,
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # If there are posts to retrieve, recursively calls function,
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Returns final list of hot post titles,
    return hot_listi 
