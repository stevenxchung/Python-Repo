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
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class Solution:
    def __init__(self, debug=False):
        self.global_feed = []  # (id, user_id)
        heapq.heapify(self.global_feed)
        self.following_map = defaultdict(set)  # { user_id: set(ids) }
        self.debug = debug

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.global_feed, (-tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        i = 0
        while i < len(self.global_feed):
            curr_post = self.global_feed[i]
            if len(feed) == 10:
                if self.debug:
                    print(feed)
                return feed
            if (
                curr_post[-1] == userId
                or curr_post[-1] in self.following_map[userId]
            ):
                feed.append(-curr_post[0])
            i += 1

        if self.debug:
            print(feed)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].remove(followeeId)


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
print(f'Runtime for our solution: {time() - sol_start}')
