import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    freq_table = defaultdict(int)
    for char in text:
        freq_table[char] += 1
    return freq_table

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        heapq.heappush(heap, internal_node)

    return heap[0]

def generate_huffman_codes(node, prefix='', huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}

    if node:
        if node.char is not None:
            huffman_codes[node.char] = prefix
        generate_huffman_codes(node.left, prefix + '0', huffman_codes)
        generate_huffman_codes(node.right, prefix + '1', huffman_codes)

    return huffman_codes

def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

def decode_text(encoded_text, huffman_tree):
    decoded_text = []
    current_node = huffman_tree
    for bit in encoded_text:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = huffman_tree
    return ''.join(decoded_text)

def compare_size(original_text, encoded_text):
    original_size = len(original_text) * 8
    encoded_size = len(encoded_text)
    print(f"Original size: {original_size} bits")
    print(f"Compressed size: {encoded_size} bits")
    compression_ratio = original_size / encoded_size
    print(f"Compression ratio: {compression_ratio:.2f}")

if __name__ == '__main__':
    text = "huffman coding is fun"
    
    freq_table = build_frequency_table(text)
    print("Frequency Table:")
    for char, freq in freq_table.items():
        print(f"{char}: {freq}")
    
    huffman_tree = build_huffman_tree(freq_table)
    
    huffman_codes = generate_huffman_codes(huffman_tree)
    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
    
    encoded_text = encode_text(text, huffman_codes)
    print("\nEncoded Text:")
    print(encoded_text)
    
    decoded_text = decode_text(encoded_text, huffman_tree)
    print("\nDecoded Text:")
    print(decoded_text)
    
    compare_size(text, encoded_text)

#python code finished