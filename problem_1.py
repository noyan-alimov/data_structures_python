class Node(object):
    
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList(object):

    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.double_linked_list = DoubleLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:

            return self.cache[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
