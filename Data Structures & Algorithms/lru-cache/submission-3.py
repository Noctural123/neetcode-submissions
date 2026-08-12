class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.remove(self.store[key])
        self.insert(self.store[key])
        return self.store[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        
        self.store[key] = Node(key, value)
        self.insert(self.store[key])

        if len(self.store) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]
    

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node



