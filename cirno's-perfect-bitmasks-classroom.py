def solve():
    x = int(input())
    
    if x == 1:
        print(3)
    elif bin(x).count("1") == 1:
        print(x+1)
    else:
        k = 0
        while (1 << k) & x == 0:
            k += 1
        print(1 << k)

t = int(input())
for _ in range(t):
    solve()
