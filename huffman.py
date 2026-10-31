import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman codes by traversing the tree
def huffman_codes(root, code, codes_dict):
    if root is None:
        return
    # Leaf node: store the code
    if root.char is not None:
        codes_dict[root.char] = code or "0"   # handles single-character input
        return
    huffman_codes(root.left, code + "0", codes_dict)
    huffman_codes(root.right, code + "1", codes_dict)


# Main Huffman encoding function
def huffman_encoding(data):
    # Count frequency of each character
    freq_dict = {}
    for char in data:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # Min heap of leaf nodes
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate codes
    root = heap[0]
    codes_dict = {}
    huffman_codes(root, "", codes_dict)
    return codes_dict


# Driver code
data = input("Enter the string to encode: ")
if not data:
    print("Empty input.")
else:
    codes = huffman_encoding(data)

    print("\nHuffman Codes for each character:")
    for char, code in codes.items():
        print(f"{char!r}: {code}")

    encoded_data = "".join(codes[char] for char in data)
    print("\nEncoded string:")
    print(encoded_data)