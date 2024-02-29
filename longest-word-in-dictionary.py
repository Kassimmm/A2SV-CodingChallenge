class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = 0
        self.ans = ""

    def insert(self, word: str) -> None:
        if not self.ans:
            self.ans = word
            self.res = len(word)
        elif len(word) > self.res:
            self.res = len(word)
            self.ans = word

        curr = self.root
        for char in word: 
            if char not in curr.children: 
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end = True
        return self.ans

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        temp = set(words)
        words.sort()
        
        output = ""
        for word in words:
            if len(word) == 1 or trie.search(word[:-1]):
                output = trie.insert(word)

        return output
