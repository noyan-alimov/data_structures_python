import sys

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.next = None
        self.previous = None
        self.left_child = None
        self.right_child = None
        self.bit = ''


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, new_node):  
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
            print(node.character, node.frequency)
            node = node.next


def create_huffman_tree(p_queue):
    if p_queue.head == p_queue.tail:
        return p_queue

    node1 = p_queue.remove_head()
    node2 = p_queue.remove_head()
    new_node = Node(None, node1.frequency + node2.frequency)
    new_node.left_child = node1
    new_node.right_child = node2
    p_queue.add(new_node)
    output = create_huffman_tree(p_queue)
    return output


def assign_bits_to_nodes(p_queue):
    node = p_queue.head

    def traverse(node):
        if node:
            if node.left_child:
                node.left_child.bit = '0'
                traverse(node.left_child)
            if node.right_child:
                node.right_child.bit = '1'
                traverse(node.right_child)
    
    traverse(node)

    return p_queue


def generate_unique_binary_code_for_each_char(tree):
    node = tree.head
    huffman_codes = {}
    return return_generate_code(node, huffman_codes)


def return_generate_code(node, huffman_codes):
    if node.left_child is None and node.right_child is None:
        huffman_codes[node.character] = node.bit
    
    if node.left_child:
        node.left_child.bit = node.bit + node.left_child.bit
        return_generate_code(node.left_child, huffman_codes)

    if node.right_child:
        node.right_child.bit = node.bit + node.right_child.bit
        return_generate_code(node.right_child, huffman_codes)

    return huffman_codes


def huffman_encoding(data):
    chars = {}
    for char in data:
        chars[char] = chars.get(char, 0) + 1
    
    p_queue = PriorityQueue()
    for character, frequency in chars.items():
        new_node = Node(character, frequency)
        p_queue.add(new_node)
    
    huffman_tree = create_huffman_tree(p_queue)
    tree_with_bits = assign_bits_to_nodes(huffman_tree)
    huffman_codes = generate_unique_binary_code_for_each_char(tree_with_bits)

    encoded_data = ''
    for char in data:
        for char2, code in huffman_codes.items():
            if char == char2:
                encoded_data += code

    return encoded_data, tree_with_bits


def huffman_decoding(data, tree):
    decoded = ''
    node = tree.head

    if node.left_child is None and node.right_child is None:  # if node is a leaf
        decoded += node.character
        return decoded

    for num in data:
        if node:
            if num == '0':
                node = node.left_child
            elif num == '1':
                node = node.right_child
            
            if node.left_child is None and node.right_child is None:
                decoded += node.character
                node = tree.head

    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))