class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        key = ord(target)
        left, right = 0, len(letters)-1

        while left < right:
            mid = (left + right) // 2
            
            if ord(letters[mid]) > key:
                right = mid
            else:
                left = mid + 1

        if ord(letters[left]) > key:
            return letters[left]
        else:
            return letters[0]
