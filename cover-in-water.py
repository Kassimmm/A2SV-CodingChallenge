t = int(input())

for _ in range(t):
    n = int(input())
    arr = input()
   
    if "..." in arr:
        print(2)
    else:
        print(arr.count("."))
    
