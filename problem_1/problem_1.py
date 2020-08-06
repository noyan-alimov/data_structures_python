class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def remove(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        return

    def remove_head(self):
        value = self.head.value
        self.head = self.head.next
        return value


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.recents = LinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache.keys():
            self.recents.remove(self.cache[key])
            self.recents.append(self.cache[key])
            return self.cache[key]
        
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.cache.keys():
            self.recents.append(value)
            self.cache[key] = value

        if len(self.cache.keys()) > 5:
            old_value = self.recents.remove_head()
            del self.cache[old_value]


our_cache = LRU_Cache(5)

def test_set(test_case, test_case2):
    our_cache.set(test_case, test_case2)
    if test_case in our_cache.cache and test_case2 in our_cache.cache:
        print('Test Success')
    else:
        print('Test Failed')

def test_get_success(test_case):
    answer = our_cache.get(test_case)
    if answer == 1:
        print('Test Success')
    else:
        print('Test Failed')

def test_get_none(test_case):
    answer = our_cache.get(test_case)
    if answer == -1:
        print('Test Success')
    else:
        print('Test Failed')

def test_get_fail(test_case):
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.get(1)       
    our_cache.get(2)       
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    answer = our_cache.get(test_case)
    if answer == -1:
        print('Test Success')
    else:
        print('Test Failed')


our_cache2 = LRU_Cache(None)

def test_set2(test_case, test_case2):
    our_cache2.set(test_case, test_case2)
    if test_case in our_cache2.cache and test_case2 in our_cache2.cache:
        print('Test Failed')
    else:
        print('Test Success')

test_set(1, 1)  # expect to successfully set to cache
test_get_success(1)  # should return 1, get value from cache
test_get_none(None)  # should return -1, edge case 1
test_get_fail(3)  # testing the linked list to handle the recent and most unrecent items logic, should return -1, edge case 2
test_set2(1, 2)  # expect setting cache to fail because the capacity is None