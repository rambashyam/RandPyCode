import TrieNode


class Trie(object):

    def __init__(self):
        self.root = TrieNode("")

    # function to insert into the Trie

    def insert(self, word):
        node = self.root

        # loop through each character in the word
        # check if there is no child containing the character.
        # If there is no child then create a new Trie node

        for char in word:
            if char in node.children:
                # add the node to the list of children in the node map
                # if the character is found assign the child node to the node variable
                node = node.children[char]
            else:
                # If the character is not found then create a new Trie node
            new_node = TrieNode(char)
            # add it to the list of children
            node.children[char] = new_node

        # Mark the end of word as true
        node.is_end = True

        # Increment counter to indicate that we see this word once more
        node.counter += 1


    def dfs (self, node, prefix):
        """ This is a depth first traversal of the trie
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        # base case, after we reach the end of the word then we append to an output list
        if node.is_end:
            self.output.append ((prefix + node.char, node.counter ))
        # else search the remainder of the trie
        # take
        for child in node.children.values():
            self.dfs(child, prefix+node.char)

    def query(self, x):
        """ Given an input (a prefix) retrieve all the words stored in the trie with that prefix.
        Sort the words by the number of times they have been inserted"""

        # Use a variable to keep track of all possible outputs.
        # There cannot be more than one word with such prefix
        # Remember the root node does not store a character and instead stored only the reference to the child nodes

        self.output = []
        node = self.root

        # Check if the prefix is in the trie

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # Return empty as you cannot find the char
                return []

        # traverse trie to get all candidates
        self.dfs(self, x[:-1])

        # sort results in reverse order and return
        return sorted(self.output, key = lambda x:x[1], reverse=True)

