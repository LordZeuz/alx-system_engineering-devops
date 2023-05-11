#!/usr/bin/python3
"""Function to return title of first 10 hot list"""
import requests


def top_ten(subreddit):
    """top 10 titles on hottest post on subredit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0)"
    }
    params = {
                "limit": 10
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
