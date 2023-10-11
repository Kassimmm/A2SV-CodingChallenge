from collections import defaultdict

n, m = map(int, input().split())
temp = []
for _ in range(n+m):
    string = input()
    temp.append(string)

hashmap = defaultdict(list)
for i in range(n+m):
    if i > (n-1):
        if hashmap[temp[i]] == []:
            print(-1)
        else:
            print(" ".join(map(str, hashmap[temp[i]])))
    else:
        hashmap[temp[i]].append(i+1)
