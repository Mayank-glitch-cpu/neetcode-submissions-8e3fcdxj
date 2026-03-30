import heapq
class Twitter:

    def __init__(self):
        self.time=0
        self.post_heap=[]
        self.get_heap=[]
        self.follow_map={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        meta= [self.time,userId,tweetId]
        heapq.heappush(self.post_heap,[-meta[0],meta])

    def getNewsFeed(self, userId: int) -> List[int]:
        count=0
        res=[]
        followees= self.follow_map.get(userId,set())
        followees.add(userId)
        
        post_copy= self.post_heap[:]
        while post_copy and count < 10:
            _,meta= heapq.heappop(post_copy)
            time,user,tweet =meta
            if user in followees:
                res.append(tweet)
                count+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].add(followeeId)
        else:
            follow_set=set()
            follow_set.add(followeeId)
            self.follow_map[followerId]=follow_set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].discard(followeeId)
        else:
            return None