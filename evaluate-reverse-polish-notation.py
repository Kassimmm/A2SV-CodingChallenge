class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for string in tokens:
            if string == "+":
                stack.append(stack.pop() + stack.pop())
            elif string == "*":
                stack.append(stack.pop() * stack.pop())
            elif string == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif string == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(string))
            
        return stack[0]
        
