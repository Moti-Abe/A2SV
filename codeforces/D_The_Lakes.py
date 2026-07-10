t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ops = []

    min_idx = a.index(min(a))
    max_idx = a.index(max(a))

    for i in range(n):
        if a[i] % 2 != a[min_idx] % 2:
            ops.append((min_idx + 1, i + 1))
        else:
            ops.append((i + 1, max_idx + 1))

    print(len(ops))
    for l, r in ops:
        if l != r:
            print(l, r)