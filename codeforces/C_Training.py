import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:1 + n]))

# Sort in descending order: a[0] is the largest
a.sort(reverse=True)

ans = 0
cur_min = float('inf')
for k in range(1, n + 1):
    # c[k] = a[k-1] + k - 1  (1-based)
    c = a[k - 1] + k - 1
    cur_min = min(cur_min, c)
    if cur_min >= k:
        ans = k

print(ans)