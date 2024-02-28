
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.min_len = float('inf')

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        self.min_len = min(self.min_len, len(word))

    
    def preFind(self):
        res = ""
        curr = self.root

        while curr.children.count(None) == 25 and len(res) < self.min_len:
            for i in range(26):
                if curr.children[i]:
                    res += chr(i+97)
                    curr = curr.children[i]
                    break 

        return res




class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for i in strs:
            trie.insert(i)

        return trie.preFind()


        
