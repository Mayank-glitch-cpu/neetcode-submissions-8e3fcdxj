class Node:

    def __init__(self,key,val):
        self.key= key
        self.val = val
        self.next= None
        self.prev= None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache= {}
        self.capacity = capacity
        self.head = self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def remove(self,node):
        nxt, prev= node.next, node.prev
        nxt.prev, prev.next = prev, nxt

    def add(self, node):
        nxt= self.head.next
        nxt.prev= self.head.next = node
        node.prev, node.next= self.head, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]= Node(key,value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU= self.tail.prev
            self.remove(LRU)
            del self.cache[LRU.key]