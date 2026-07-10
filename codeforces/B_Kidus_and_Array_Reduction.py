
t = int(input())
    
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res_arr = arr.copy()
    count = 0
    while res_arr:
        # get the index of the maximum element in the array from back
        max_val = max(res_arr)
        ind = len(res_arr) - 1 - res_arr[::-1].index(max_val)
        del res_arr[ind:]
        count += 1

    print(count)