class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for employee in employees:
            ID, IMPT, SUB = employee.id, employee.importance, employee.subordinates
            graph[ID] = [IMPT, SUB]

        visited, count = set(), 0
        def dfs(ID):
            nonlocal count
            visited.add(ID)
            count += graph[ID][0]

            for node in graph[ID][1]:
                if node not in visited:
                    dfs(node)
        dfs(id)
        return count
