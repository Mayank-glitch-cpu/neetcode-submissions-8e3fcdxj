# import heapq
# class Twitter:

#     def __init__(self):
#         self.time=0
#         self.post_heap=[]
#         self.follow_map={}

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         self.time+=1
#         meta= [self.time,userId,tweetId]
#         heapq.heappush(self.post_heap,[-meta[0],meta])

#     def getNewsFeed(self, userId: int) -> List[int]:
#         count=0
#         res=[]
#         followees= self.follow_map.get(userId,set())
#         followees.add(userId)
        
#         post_copy= self.post_heap[:]
#         while post_copy and count < 10:
#             _,meta= heapq.heappop(post_copy)
#             time,user,tweet =meta
#             if user in followees:
#                 res.append(tweet)
#                 count+=1
#         return res

#     def follow(self, followerId: int, followeeId: int) -> None:
#         if followerId in self.follow_map:
#             self.follow_map[followerId].add(followeeId)
#         else:
#             follow_set=set()
#             follow_set.add(followeeId)
#             self.follow_map[followerId]=follow_set

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         if followerId in self.follow_map:
#             self.follow_map[followerId].discard(followeeId)
#         else:
#             return None

# ---------------- optimised ----------------
class Twitter(object):

    def __init__(self):
        self.time=0
        self.user_tweet=defaultdict(list)
        self.follow_map={}

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time+=1
        self.user_tweet[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res=[]
        followees= self.follow_map.get(userId,set())
        followees.add(userId)
        max_heap=[]
        for uid in followees:
            for t , tid in self.user_tweet[uid][-10:]:
                heapq.heappush(max_heap,(-t,tid))
        while max_heap and len(res)<10:
            _,tweetId=heapq.heappop(max_heap)
            res.append(tweetId)
            
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.follow_map:
            self.follow_map[followerId].add(followeeId)
        else:
            follow_set=set()
            follow_set.add(followeeId)
            self.follow_map[followerId]=follow_set

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.follow_map:
            self.follow_map[followerId].discard(followeeId)
        else:
            return None


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)