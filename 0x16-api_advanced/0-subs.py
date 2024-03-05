#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    If an invalid subreddit is given, the function will return 0.
    """
    # Set the custom user-agent header
    headers = {'User-Agent': 'python3:0-subs:v1.0 (by /u/wintermancer)'}

    # Make a GET request to the subreddit endpoint
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers)

    # Check the status code and the redirect flag
    if response.status_code == 200 and not response.json().get('data').get('over18'):
        # Return the number of subscribers
        return response.json().get('data').get('subscribers')
    else:
        # Return 0 for invalid subreddit
        return 0

