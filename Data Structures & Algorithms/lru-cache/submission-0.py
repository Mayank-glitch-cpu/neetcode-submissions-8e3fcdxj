class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.next = self.prev= None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} # hash map to store the pointer   

        # a left and a right pointer to get the LRU and MRU
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self,node):
        prev,nxt= node.prev, node.next
        prev.next,nxt.prev= nxt,prev

    def insert(self,node): # will be always be inserted  at the end 
        prev=self.right.prev
        prev.next=self.right.prev=node
        node.prev, node.next= prev,self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]= Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru= self.left.next # get the least recently used node 
            self.remove(lru) # remove it from list
            del self.cache[lru.key] # delete this key from hash map

       
