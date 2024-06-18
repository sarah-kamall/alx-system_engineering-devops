#!/usr/bin/python3

"""
    function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0
"""


import requests


def number_of_subscribers(subreddit):
    """
        queries the Reddit API and
        returns the number of subscribers
    """
    ENDPOINT = 'http://www.reddit.com/r/' + subreddit + '/about.json'
    HEADERS = {
        "User-Agent": "Custom"
    }
    RESPONSE = requests.get(ENDPOINT, headers=HEADERS, allow_redirects=False, )
    if RESPONSE.status_code != 200:
        return 0
    else:
        return RESPONSE.json().get("data").get("subscribers")
