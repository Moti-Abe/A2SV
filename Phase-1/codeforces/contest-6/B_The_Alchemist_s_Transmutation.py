t = int(input())

while t > 0:
    t -= 1

    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    
    min_num = min(arr)
    max_num = max(arr)
    if min_num <= x <= max_num:
        print("YES")
    else:
        print("NO")
