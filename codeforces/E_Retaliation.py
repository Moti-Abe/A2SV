import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # n >= 2 by constraints
    denom = n * n - 1

    a1 = a[0]
    an = a[-1]

    y_num = n * a1 - an
    x_num = n * an - a1

    # Check divisibility
    if y_num % denom != 0 or x_num % denom != 0:
        print("NO")
        continue

    y = y_num // denom
    x = x_num // denom

    # Non-negativity
    if x < 0 or y < 0:
        print("NO")
        continue

    ok = True
    # Verify all positions
    for i in range(n):
        idx = i + 1  # 1-based index
        expected = x * idx + y * (n - idx + 1)
        if expected != a[i]:
            ok = False
            break

    print("YES" if ok else "NO")
