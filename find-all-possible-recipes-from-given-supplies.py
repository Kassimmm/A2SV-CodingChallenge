class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        res = set()

        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                hashmap[recipes[i]] += 1
        
        for i in graph:
            if i not in hashmap and i in supplies:
                queue.append(i)

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                res.add(node)
                for neigh in graph[node]:
                    hashmap[neigh] -= 1
                    if hashmap[neigh] == 0:
                        queue.append(neigh)

        return [i for i in recipes if i in res]
