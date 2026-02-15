t = int (input())

while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))

    sum = 0
    for i in range (n):
        sum += arr[i]
    
    count = 0
    if sum%n != 0:
        print(-1)
    else:
        for i in range(n):
            if arr[i] > sum/n:
                count += 1
        print(count)

