class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid(state):
            return True

        def get_candidates(state):
            arr = []
            if not state:
                arr = nums.copy()
            else:
                for num in nums: 
                    if num > max(state):
                        arr.append(num)
            return arr

        def search(state, solution):
            if is_valid(state):
                solution.append(state.copy())
            
            candidates = get_candidates(state)
            for candidate in candidates:
                state.append(candidate)
                search(state, solution)
                state.pop()

        state, solution = [], []
        search(state, solution)
        return solution
        
