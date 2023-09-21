t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    
    target = (a + b) // 4
    mini = min(a,b)
    print(min(target, mini)) 
