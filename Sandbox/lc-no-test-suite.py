from collections import defaultdict
import heapq
from math import inf
from time import time
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Node:
    def __init__(self, key=0, val=0):
        '''Doubly Linked-list Node'''
        self.key, self.val = key, val
        self.prev = self.next = None


class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        self.follow_map = defaultdict(set)  # { user_id: Set[user_id] }
        # Tweets are treated as timestamps where t + 1 should be shown before t
        self.tweet_map = defaultdict(list)  # { user_id: List[tweet] }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        # Add tweets from user's feed
        for t in self.tweet_map[userId]:
            # Negative value since we are using max-heap
            feed.append(-t)

        # Add tweets from followees
        for followee_id in self.follow_map[userId]:
            for t in self.tweet_map[followee_id]:
                # Negative value since we are using max-heap
                feed.append(-t)

        # Transform feed in to heap where most recent tweets are shown first
        heapq.heapify(feed)

        top_ten_tweets = []
        for t in feed:
            if len(top_ten_tweets) == 10:
                break
            # Reverse the negative value from max-heap
            top_ten_tweets.append(-t)

        if self.debug:
            print(f'Most recent tweets for user={userId}: {top_ten_tweets}')
        return top_ten_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].remove(followeeId)


if __name__ == '__main__':
    test = Solution(debug=True)
    sol_start = time()
    # User 1 posts a new tweet(id = 5)
    test.postTweet(1, 5)
    # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    test.getNewsFeed(1)
    # User 1 follows user 2
    test.follow(1, 2)
    # User 2 posts a new tweet(id=6)
    test.postTweet(2, 6)
    # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5
    test.getNewsFeed(1)
    # User 1 unfollows user 2
    test.unfollow(1, 2)
    # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2
    test.getNewsFeed(1)
    print(f'Runtime for our solution: {time() - sol_start}\n')
