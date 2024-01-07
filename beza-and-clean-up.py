n, m, s, a, b = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort(reverse=True)
arrB.sort(reverse=True)

preA, preB = [0] * (n+1), [0] * (m+1)

for i in range(1, n+1):
    preA[i] = arrA[i-1] + preA[i-1]
    
for i in range(1, m+1):
    preB[i] = arrB[i-1] + preB[i-1]

ans, curr = 0, 0

for i in range(n+1):
    remaining_weight = s - (i * a)
    remaining_weight_b = min(m, remaining_weight // b)
    
    if remaining_weight < 0:
        break
    curr = preA[i] + preB[remaining_weight_b]
    ans = max(ans, curr)

print(ans)
