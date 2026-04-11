t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if a[i] > b[i]:
            a.insert(i, b[i])
            a.pop()
            count += 1
            
    print(count)