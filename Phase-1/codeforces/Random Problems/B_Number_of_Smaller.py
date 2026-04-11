n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

left, right = 0, 0
res = []
while right <  m and left < n:
    if b[right] > a[left]:
        left += 1
    else:
        res.append(left)
        right += 1
while right < m:
    res.append(n)
    right += 1

print(*res)
