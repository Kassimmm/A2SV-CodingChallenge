t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    infected = list(map(int, input().split()))
    infected.sort()
    removed = 0
    protected = 0
    towns = []

    for idx, current_infected in enumerate(infected):
        next_infected = infected[(idx + 1) % m]
        size = 0

        if idx < m - 1:
            size = next_infected - current_infected - 1
        else:
            size = n - current_infected + next_infected - 1

        towns.append(size)


    towns.sort(reverse = True)

    for town_size in towns:
        current_size = town_size - removed
        
        if current_size > 1:
            protected += current_size - 1
            removed += 4
        elif current_size == 1:
            protected += 1
            removed += 2

    print(n - protected)
