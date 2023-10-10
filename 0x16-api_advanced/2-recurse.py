#!/usr/bin/python3
""" 2. Recurse it! """
import requests
import time


def recurse(subreddit, hot_list=[], after="", retries=60):
    """ Write a recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit """
    headers = {"User-Agent": "AmrShoukry"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()
        new_after = data['data']['after']
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        if new_after is None:
            return hot_list

        remaining_req = int(response.headers.get('X-Ratelimit-Remaining', 0))
        reset_time = int(response.headers.get('X-Ratelimit-Reset', 0))

        if remaining_req <= 1:
            sleep_time = max(0, reset_time - time.time())
            time.sleep(sleep_time)

        return recurse(subreddit, hot_list, new_after, retries)
    elif response.status_code == 429:
        time.sleep(1)
        return recurse(subreddit, hot_list, after, retries)
    else:
        return None
