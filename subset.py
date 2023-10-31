class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid(state):
            return len(state) <= len(nums)

        def get_candidates(state):
            arr = []
            if not state:
                arr = nums.copy()
            else:
                for i in nums: 
                    if i > max(state):
                        arr.append(i)
            return arr

        def search(state, solution):
            if is_valid(state):
                solution.append(state.copy())
            else:
                return 
            
            candidates = get_candidates(state)
            for candidate in candidates:
                state.append(candidate)
                search(state, solution)
                state.pop()

        state, solution = [], []
        search(state, solution)
        return solution
        
