t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    i, j, k = 0, 1 , 2

    isexits = False
    while k < n:
        if h[i] < h[j] and h[j] > h[k]:
            isexits = True
            break
        i += 1
        j += 1
        k += 1 
    
    if isexits:
        print("YES")
        print(i+1, j+1, k+1)
    else:
        print("NO")