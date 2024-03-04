class TrieNode:
    def __init__(self):
        self.is_end = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> int:
        curr = self.root
        for char in word: 
            if char not in curr.children: 
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.is_end += 1
            

    def startsWith(self, prefix: str) -> bool:
        total = 0
        curr =  self.root

        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
            total += curr.is_end

        return total
          


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]: 
        trie = Trie()
        output = []

        for word in words:
            trie.insert(word)

        for word in words:
            output.append(trie.startsWith(word))
        
        return output
