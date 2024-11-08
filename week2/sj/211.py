class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True

    def search_by_node(self, word, node):
        for idx, c in enumerate(word):
            if c == '.':
                for child in node.children:
                    if self.search_by_node(word[idx + 1:], node.children[child]):
                        return True
                return False
            if c not in node.children:
                return False
            node = node.children[c]
        if node.end:
            return True
        return False

    def search(self, word: str) -> bool:
        return self.search_by_node(word, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
