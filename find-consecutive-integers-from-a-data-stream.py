class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        
        if len(self.stream) > self.k:
            removed_num = self.stream.popleft() 
            if removed_num == self.value:
                self.count -= 1
        
        if num == self.value:
            self.count += 1
        
        return self.count == self.k
