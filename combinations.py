class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def is_valid(state):
            return len(state) == k

        def get_candidates(state):
            arr = []
            if not state:
                for i in range(1, n+1):
                    arr.append(i)
            else:
                for i in range(state[-1]+1, n+1):
                    arr.append(i)
            return arr

        def search(state, solutions): 
            if is_valid(state):
                solutions.append(state.copy())
                return 
            candidates = get_candidates(state)
            for candidate in candidates:
                state.append(candidate)
                search(state, solutions)
                state.pop()

        state, solutions = [], [] 
        search(state, solutions)
        return solutions 

        

        

