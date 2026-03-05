n = int(input())
arr = list(map(int, input().split()))

has_even = False
for num in arr:
    if num % 2 == 0:
        has_even = True
        break

has_odd = False
for num in arr:
    if num % 2 != 0:
        has_odd = True
        break
if has_even and has_odd:
    arr.sort()
print(*arr) 