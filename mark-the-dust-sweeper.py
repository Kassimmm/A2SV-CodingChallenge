t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr[:n-1] == [0] * (n-1):
        print(0)
    else:
        j = 0
        for i in range(n):
            if arr[i] != 0:
                j = i
                break
        x = sum(arr[j:-1])
        y = arr[j:-1].count(0)

        print(x+y)
