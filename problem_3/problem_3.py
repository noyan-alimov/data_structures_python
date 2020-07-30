import sys

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.next = None
        self.previous = None
        self.left_child = None
        self.right_child = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, character, frequency):  
        new_node = Node(character, frequency)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        node = self.head
        while (node and node.frequency <= new_node.frequency):
            node = node.next

        if node == self.head:   # if new node's frequency is the least compared to any other node's frequencies, we prepend the new node
            new_node.next = self.head
            self.head.previous = new_node
            self.head = self.head.previous
            return

        if node is None:   # if new node's frequency is the largest compared to other node's frequencies, we append the new node
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = self.tail.next
            return

        before_new_node = node.previous   # if we need to add new node in between the queue
        before_new_node.next = new_node
        node.previous = new_node
        new_node.previous = before_new_node
        new_node.next = node

    def remove_head(self):
        node_to_remove = self.head
        self.head = self.head.next
        return node_to_remove

    def __repr__(self):
        node = self.head
        while node:
            print(node.frequency)
            node = node.next

        


queue = PriorityQueue()
queue.add('A', 3)
queue.add('B', 2)
queue.add('C', 7)
queue.add('D', 5)
queue.__repr__()




# def huffman_encoding(data):
#     chars = {}
#     for char in data:
#         chars[char] = chars.get(char, 0) + 1
#     return chars

# def huffman_decoding(data, tree):
#     pass

# print(huffman_encoding('AAABBCCD'))



























# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))