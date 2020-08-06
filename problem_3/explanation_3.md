Data structures used:
- Min-heap was used to implement priority queue, which was to enable inserting nodes in between the nodes and sorting the priority queue from least to most frequency.
The add and remove_head methods are working in O(1) time.
- Dictionaries were used to store the characters with their specific frequency data.
In huffman_encoding function the operation is run in O(n log n) time. There is a for loop inside a for loop, but the if statement after helps to decrease the time operation. It runs at O(1) space because it creates the appropriate data structures and variables only once when the function is called.
huffman_decoding, return_generate_code, assign_bits_to_nodes and create_huffman_tree functions are run in O(n) time, huffman_decoding uses a for loop while the others use recursion. These functions run at O(1) space except create_huffman_tree function. create_huffman_tree runs at O(n) space because it creates a new_node every time due to recursion.