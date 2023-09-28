class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2

"""
class Solution(object):
    def smallestEvenMultiple(self, n):
        last_factor = (n * 2) + 1
        for num in range(1, last_factor):
            if num % 2 == 0 and num % n == 0:
                return num
This is the brute force approach
"""
