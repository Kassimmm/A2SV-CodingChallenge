class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0 for _ in range(len(s)+2)]
        res = []
    
        for start, end, k in shifts:
            k = -1 if k == 0 else 1
             
            arr[start+1] += k
            arr[end+2] -= k
        
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        
        for i in range(1, len(arr)-1):
            arr[i] += (ord(s[i-1]) - 97)
            arr[i] %= 26
            arr[i] += 1

            res.append(chr(arr[i]+96))
        
        return "".join(map(str, res))
