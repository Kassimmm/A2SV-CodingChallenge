class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "]" : "[", "}" : "{"}

        for string in s:
            if string in hashmap:
                if stack and stack[-1] == hashmap[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)

        return True if not stack else False
