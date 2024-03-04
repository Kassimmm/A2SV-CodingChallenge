class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def find_max_xor(self, word: str) -> str:
        res = ""
        curr = self.root

        for i in range(len(word)):
            turn = str(1 - int(word[i])) 
            if turn not in curr.children:
                res += word[i]
                curr = curr.children[word[i]]
            else:
                res += turn
                curr = curr.children[turn]
                
        return res



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_bit = max(nums).bit_length()
        for num in nums:
            binary_num = "0" * (max_bit - len(bin(num)[2:])) + bin(num)[2:] 
            trie.insert(binary_num)

        res = 0
        for num in nums:
            binary_num = "0" * (max_bit - len(bin(num)[2:])) + bin(num)[2:] 
            temp = trie.find_max_xor(binary_num)
            res = max(res, int(temp, 2) ^ num)
            
            if res == (2 ** max_bit) -1:
                return res

        return res
