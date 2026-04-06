n = int(input())
arr = list(map(int,input().split()))
max_rest = 0
count = 0
for i in range(n):
    if arr[i] == 1:
        count += 1
        max_rest = max(count, max_rest)
    else:
        count = 0

count = 0
l, r = 0, n-1
while arr[l] == 1:
    count += 1
    l+= 1
while arr[r] == 1:
    count += 1
    r-=1

max_rest = max(max_rest,count)

print(max_rest)