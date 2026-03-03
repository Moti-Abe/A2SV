t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    a = arr[1] - arr[0]
    b = arr[2] - arr[1]
    min_num = a + b
    for i in range(n-2):
        a = arr[i+1] - arr[i]
        b = arr[i+2] - arr[i+1]
        total = a+b
        min_num = min(min_num,total)
    print(min_num)
