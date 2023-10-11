a = list(map(int, input().split()))
n = int(input())
flag = True
for _ in range(n):
    temp = list(map(int, input().split()))
    res = set(temp).difference(set(a))
    if res:
        flag = False
print(flag)
