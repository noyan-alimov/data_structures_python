Data Structures used:
- Dictionary:
It was used to work as cache to handle operations such as insert, lookup and delete in O(1) time.

- Linked list
It was used to store values in recent order. When our cache was full, linked list helped to remove least used items from cache. The operations are handled in O(1) time. Although the remove method is questionable because it traverses the linked list to remove a specific item, our linked list's size is very short due to cache limit capacity, so we can say that this method is operated in O(1) time.

