t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int , input().split()))

    arr.sort()
    left , right = 2, n-2

    crowd_sum = arr[0] + arr[1]
    elite = arr[n-1]
    isYes = False
    while left < right:
        if  crowd_sum < elite:
            print("YES")
            break
    else:
        crowd_sum += arr[left]
        elite += arr[right]
        left += 1
        right -= 1
    
    if not (isYes):
        print("NO")
    