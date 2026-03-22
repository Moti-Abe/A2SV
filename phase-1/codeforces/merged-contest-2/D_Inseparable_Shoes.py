t = int(input())

for _ in range(t):
    n = int(input())
    shoes = list(map(int, input().split()))

    p = [0] * n
    i = 0
    ispossible = True
    while i < n:
        start = i
        while i < n and shoes[i] == shoes[start]:
            i += 1
        len = i - start
        if len == 1:
            ispossible = False
            break
        
        for k in range(start, i):
            p[k] = k + 2
        p[i - 1] = start + 1

    if ispossible:
        print(*p)
    else:
        print(-1)