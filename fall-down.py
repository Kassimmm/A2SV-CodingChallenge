def func():
    n,m = list(map(int,input().split()))
    grid = []
    for i in range(n):
        grid.append(list(input()))
    
    for r in range(n-1,-1,-1):
        for c in range(m-1,-1,-1):
            if grid[r][c] == "*":
                i = r
                while i+1 < n and grid[i+1][c] == '.':
 
                    grid[i][c] = "."
                    grid[i+1][c] = "*"
                    i+=1
 
 
    for row in grid:
        print("".join(row))      
    print()
 
t = int(input())
for _ in range(t):
    func()
