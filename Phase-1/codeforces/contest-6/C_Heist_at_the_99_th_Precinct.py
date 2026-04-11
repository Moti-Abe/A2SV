t = int(input())

while t > 0:
    t -= 1
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_num = max(arr)
    count_max = arr.count(max_num)

    next_max = 0
    for i in range(len(arr)-1,0):
        if arr[i] < max_num:
            next_max = arr[i]
    count_next_max = arr.count(next_max)

    
    if count_max%2 == 0:
        if count_next_max == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES") 