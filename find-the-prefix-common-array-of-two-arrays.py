class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        output = []
        def isCommon(t):
            arr1, arr2 = A[:t+1], B[:t+1]
            arr1.sort()
            arr2.sort()
            l= r= res= 0
            while l < len(arr1) and r < len(arr2):
                if arr1[l] == arr2[r]:
                    res += 1
                    r += 1
                    l += 1
                elif arr1[l] > arr2[r]:
                    r += 1
                elif arr1[l] < arr2[r]:
                    l += 1
            return res

        for i in range(len(A)):
            output.append(isCommon(i))

        return(output)

""" 
Optimal solution is below
"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        hashmap = defaultdict(int)

        for idx in range(len(A)):
            hashmap[A[idx]] += 1
            hashmap[B[idx]] += 1

            common_count = list(hashmap.values()).count(2)
            res.append(common_count)

        return(res)
