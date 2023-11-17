class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        hashmap = Counter(words)

        for word, freq in dict(hashmap).items():
            heap.append((-freq, word))

        heapify(heap) 
        temp = []
        for i in range(k):
            temp.append(heap[0])
            heappop(heap)
        
        res = defaultdict(list)
        for i,j in temp:
            res[i].append(j)
            
        output = []
        for index, item in dict(res).items():
            n = len(item)
            heap = item
            heapify(heap)
            while n > 1:
                output.append(heap[0])
                heappop(heap)
                n -= 1
            output.append(heap[0])

        return output
