#!/usr/bin/python3

"""
 Function that queries the Reddit API and prints the titles
 of the first 10 hot posts listed for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        queries the Reddit API and
        returns the top 10 posts
    """
    ENDPOINT = 'http://www.reddit.com/r/' + subreddit + '/hot.json'
    HEADERS = {
        "User-Agent": "Custom"
    }
    if (after is not None):
        PARAMS = {
            "after": after,
            "limit": 100
        }
    else:
        PARAMS = {
            "limit": 100,
        }
    RESPONSE = requests.get(ENDPOINT, headers=HEADERS, params=PARAMS)
    if RESPONSE.status_code != 200:
        return None
    else:
        posts = RESPONSE.json().get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get('title'))
        after = RESPONSE.json().get("data").get("after")
        if(len(posts) and after is not None):
            recurse(subreddit, hot_list, after)
    return hot_list
