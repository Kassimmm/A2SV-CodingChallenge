class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for i in range(n):
            stack.append(asteroids[i])
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                x = stack.pop()
                y = stack.pop()

                if abs(x) > abs(y):
                    stack.append(x)
                elif abs(x) < abs(y):
                    stack.append(y)

        return stack
