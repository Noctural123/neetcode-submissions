class Node:

    # Initialize nodes
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Make left and right node, attached them to each other
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Remove -> Insert to move the val we're getting to the end (make freshest)
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Create new node (doesn't matter if key already in, we removed it already)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If over cap, get lru and remove it from list and map
        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
            

    # Remove Node from linked list
    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt

    # Inserts node to end of linked list
    def insert(self, node): 
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        prev.next = nxt.prev = node

