#!/usr/bin/python3
""" 3. Count it! """
import requests
import time


def count_words(subreddit, word_list, after="", retries=60, word_dict={}):
    """ Write a recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of given keywords  """
    headers = {"User-Agent": "AmrShoukry"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(url, allow_redirects=False, headers=headers)

    word_list = [word.lower() for word in word_list]

    if response.status_code == 200:
        data = response.json()
        new_after = data['data']['after']
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            title_keywords = title.split(' ')
            for keyword in title_keywords:
                lower_key = keyword.lower()
                for word in word_list:
                    if lower_key == word:
                        word_dict[lower_key] = word_dict.get(lower_key, 0) + 1

        if new_after is None:
            if (len(word_dict) == 0):
                return
            sorted_dict = dict(sorted(word_dict.items(),
                                      key=lambda item: (item[1], item[0]),
                                      reverse=True))
            for key, value in sorted_dict.items():
                print(f"{key}: {value}")
            return

        remaining_req = int(response.headers.get('X-Ratelimit-Remaining', 0))
        reset_time = int(response.headers.get('X-Ratelimit-Reset', 0))

        if remaining_req <= 1:
            sleep_time = max(0, reset_time - time.time())
            time.sleep(sleep_time)

        return count_words(subreddit, word_list, new_after, retries, word_dict)
    elif response.status_code == 429:
        time.sleep(1)
        return count_words(subreddit, word_list, after, retries, word_dict)
    else:
        return None
