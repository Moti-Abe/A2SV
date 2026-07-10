t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    if s < s[::-1]:
        print("YES")
    elif k == 0:
        print("NO")
    elif len(set(s)) == 1:
        print("NO")
    else:
        print("YES")