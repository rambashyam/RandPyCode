class TrieNode:
    # A node in the trie structure
    def __init__(self, char):
        # character stored in the node
        self.char = char

        # whether this can be the end of the word
        self.is_end = False

        # a counter to count how many times a word is inserted
        self.counter = 0

        # dictionary of child nodes
        # keys are characters and values are nodes
        self.children = {}
