#!/usr/bin/python3

"""
 Function that queries the Reddit API and prints the titles
 of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
        queries the Reddit API and
        returns the top 10 posts
    """
    ENDPOINT = 'http://www.reddit.com/r/' + subreddit + '/hot.json'
    HEADERS = {
        "User-Agent": "Custom"
    }
    PARAMS = {
        "limit": 10
    }
    RESPONSE = requests.get(ENDPOINT, headers=HEADERS, params=PARAMS)
    if RESPONSE.status_code != 200:
        print(None)
    else:
        posts = RESPONSE.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get('title'))
