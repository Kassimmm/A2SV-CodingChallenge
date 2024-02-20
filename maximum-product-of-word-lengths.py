class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        word_bits = [0] * len(words)

        for i, word in enumerate(words):
            bits = 0
            for char in word:
                bits |= 1 << (ord(char) - ord('a'))
            word_bits[i] = bits

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if word_bits[i] & word_bits[j] == 0:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        return max_len
