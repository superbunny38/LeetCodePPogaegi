class WordDictionary:

    def __init__(self):
        self.container = []

    def addWord(self, word: str) -> None:
        self.container.append(word)
        # print("\n word added:",word)
        # print(self.container)

    def search(self, word: str) -> bool:
        def count_diff(word1, word2):
            ret = 0
            for idx in range(len(word1)):
                if word1[idx] != word2[idx]:
                    ret +=1
            #print(f"diff between {word1} and {word2}: ret")
            return ret

        if '.' in word:
            for letter in self.container:
                if len(word) != len(letter):
                    continue
                else:
                    n_diff = count_diff(letter,word)
                    if n_diff == word.count('.'):
                        return True
            return False
        else:
            return (word in self.container)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
