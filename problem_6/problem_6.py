class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    new_llist = LinkedList()
    node1 = llist_1.head
    while node1:
        new_llist.append(node1.value)
        node1 = node1.next

    node2 = llist_2.head
    while node2:
        new_llist.append(node2.value)
        node2 = node2.next
    
    return new_llist

def intersection(llist_1, llist_2):
    node1 = llist_1.head
    node_values1 = []
    while node1:
        node_values1.append(node1.value)
        node1 = node1.next

    node2 = llist_2.head
    node_values2 = []
    while node2:
        node_values2.append(node2.value)
        node2 = node2.next

    new_llist = LinkedList()
    for v in node_values1:
        if v in node_values2:
            new_llist.append(v)

    return new_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # expect a linked list that has values of the first and second linked list
print (intersection(linked_list_1,linked_list_2)) # expect a linked list that has values only that are in both first and secont linked lists


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # expect a linked list that has values of the first and second linked list
print (intersection(linked_list_3,linked_list_4)) # expect an empty linked list because there are no common values between first and second linked list


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print (union(linked_list_5,linked_list_6)) # expect an empty linked list
print (intersection(linked_list_5,linked_list_6)) # expect an empty linked list