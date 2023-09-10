class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for chunk in parts:
            if chunk == "..":
                if stack:
                    stack.pop()
            elif chunk != '.' and chunk != '':
                stack.append(chunk)
            
        return '/' + "/".join(stack)

