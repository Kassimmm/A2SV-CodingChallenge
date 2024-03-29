class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.stack.append(val)
    

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min[-1]:
                self.min.pop()
            self.stack.pop()


    def top(self) -> int:
        return self.stack[-1] if self.stack else None


    def getMin(self) -> int:
        return self.min[-1] if self.min else None
