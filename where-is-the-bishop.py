t = int(input())

for _ in range(t):
    input()
    grid = []
    output = []

    for _ in range(8):
        line = list(input())
        grid.append(line)
    for i in range(len(grid)-2):
        if grid[i].count("#") == 2 and grid[i+1].count("#") == 1 and grid[i+2].count("#") == 2 :
            output.append(i+1)

    temp = grid[output[-1]]
    for i in range(len(temp)):
        if temp[i] == "#":
            output.append(i)
    print(output[0]+1, output[-1]+1)
