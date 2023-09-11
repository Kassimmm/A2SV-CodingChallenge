class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        hashmap = {}
        for i in range(len(tickets)):
            hashmap[i] = tickets[i]

        l = count = 0
        while hashmap[k] != 0:
            if hashmap[l] == 0:
                pass
            else:
                count += 1
                hashmap[l] -= 1
            l = (l + 1) % len(tickets)
            
        return count



        
