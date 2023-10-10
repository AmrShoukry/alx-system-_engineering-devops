#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit """
    headers = {"User-Agent": "AmrShoukry"}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, allow_redirects=False, headers=headers)
    data = response.json()

    if response.status_code == 200:
        return (data['data']['subscribers'])
    return 0
