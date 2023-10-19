def func(weights):
    weights.sort()
    sum = 1
    for i in range(n):
        if weights[i] > sum:
            return sum
        sum += weights[i]
    return sum


if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))
    print(func(weights))
