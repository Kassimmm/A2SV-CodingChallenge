#optimal soclution
a = list(map(int, input().split()))
n = int(input())
flag = True
for _ in range(n):
    temp = list(map(int, input().split()))
    res = set(temp).difference(set(a))
    if res:
        flag = False
print(flag)


"""
superset = list(map(int, input().split()))
n = int(input())
subsets = []
for i in range(n):
    arr = input().split()
    subsets.extend(arr)

for i in subsets:
    if i not in superset:
        print("False")
        break
    else:
        print("True")
"""


    
    
