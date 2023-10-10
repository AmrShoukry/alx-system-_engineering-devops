#!/usr/bin/python3
""" 1. Top Ten """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed for a subreddit. """
    headers = {"User-Agent": "AmrShoukry"}
    url = f'https://www.reddit.com/r/{subreddit}/top.json?limit=10'
    response = requests.get(url, allow_redirects=False, headers=headers)
    data = response.json()

    if response.status_code == 200:
        top = data['data']['children']
        for post in top:
            print(post['data']['title'])
    else:
        print("None")
