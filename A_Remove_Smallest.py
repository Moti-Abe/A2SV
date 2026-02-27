t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ispossible = True
    for i in range (n-1):
        if abs(arr[i+1] - arr[i]) > 1:
            ispossible = False
            break
    if ispossible:
        print("YES")
    else:
        print("NO")
    
