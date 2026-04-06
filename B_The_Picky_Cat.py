
import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        arr[i] = abs(arr[i])
    val = arr[0]
    x = math.ceil(n/2)+1
    if val in arr[:x]:
        print("YES")
    else:
        print("N0")