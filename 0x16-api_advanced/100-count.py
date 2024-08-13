#!/usr/bin/python3

"""
 Function that queries the Reddit API and prints the titles
 of the first 10 hot posts listed for a given subreddit.
"""


import requests


def count_words(subreddit, word_list, after=None, count={}):
    """
        queries the Reddit API and
        returns the top 10 posts
    """

    ENDPOINT = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
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
            title = post.get("data").get('title')
            for word in word_list:
                word_comp = word.lower()
                title_comp = title.lower()
                if (word_comp in title_comp):
                    if count.get(word) is None:
                        count[word] = 0
                    count[word] += 1
        after = RESPONSE.json().get("data").get("after")
        if(after is not None):
            count_words(subreddit, word_list, after, count)
        else:
            sorted_dict = dict(sorted(count.items(), key=lambda item: item[1],
                                      reverse=True))
            for wordp, counterp in sorted_dict.items():
                print(f"{wordp.lower()}: {counterp}")
