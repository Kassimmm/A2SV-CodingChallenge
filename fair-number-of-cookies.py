class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
            state = [0]*k
            ans = sum(cookies)
            
            def search(state, idx):
                nonlocal ans
                if idx >= len(cookies):
                    ans = min(ans, max(state))
                    return
                
                for i in range(k):
                    state[i] += cookies[idx]
                    if state[i] < ans:
                        search(state, idx+1)
                    state[i] -= cookies[idx]
            
            search(state, 0)
            return ans 
