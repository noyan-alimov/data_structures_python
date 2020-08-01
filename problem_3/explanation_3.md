Data structures used:
- Min-heap was used to implement priority queue, which was to enable inserting nodes in between the nodes and sorting the priority queue from least to most frequency.
The add and remove_head methods are working in O(1) time.
- Dictionaries were used to store the characters with their specific frequency data.
In huffman_encoding function the operation is run in O(n^2) time. It uses a for loop inside a for loop to generate the encoded data. huffman_decoding, return_generate_code, assign_bits_to_nodes and create_huffman_tree functions are run in O(n) time, huffman_decoding uses a for loop while the others use recursion.