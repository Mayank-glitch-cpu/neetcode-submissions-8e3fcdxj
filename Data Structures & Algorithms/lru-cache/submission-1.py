class Node:
    def __init__(self, key, value):
        self.key= key
        self.value= value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity= capacity

        self.head = self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail , self.head

    def add(self, node):
        prev = self.tail.prev
        prev.next = self.tail.prev = node
        node.prev, node.next = prev, self.tail

    def remove(self, node):
        prev, nxt = node.prev , node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            print('debug 1')
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
