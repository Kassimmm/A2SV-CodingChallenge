class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        for j in range(len(arr)):
            hashmap[j] = arr[j] * 2

        for j in range(len(arr)):
            if (arr[j] in hashmap.values() and arr[j] != hashmap[j]) or list(hashmap.values()).count(arr[j]) > 1:
                return True
        return False

"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == 2 * arr[j] and i != j:
                    return True
                    break
            else:
                continue
            break
        else:
            return False
"""

