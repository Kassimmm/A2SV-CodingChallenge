class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []

        votes = defaultdict(int)
        incumbent = None

        for person, time in zip(persons, times):
            votes[person] += 1
            if incumbent is None or votes[person] >= votes[incumbent]:
                incumbent = person
            self.leaders.append(incumbent)

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1  
              
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        
        return self.leaders[left]
