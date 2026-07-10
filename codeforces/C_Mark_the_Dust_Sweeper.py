t = int(input())

for _ in range(t):
    n = int(input())
    dust = list(map(int, input().split()))
    
    # Skip leading zeros — dust cannot pass through them from the left
    start = 0
    while start < n and dust[start] == 0:
        start += 1

    total_operations = 0

    for i in range(start,n-1):
        if dust[i] > 0:
            total_operations += dust[i]
        else:
            total_operations += 1

    print(total_operations)

