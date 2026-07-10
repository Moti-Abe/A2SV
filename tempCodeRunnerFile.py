def fprint(ind,n,arr,nums):
    if ind >= n:
        print(arr)
        return
    
    # pick
    arr.append(nums[ind])
    fprint(ind+1, n, arr, nums)

    #backtrack
    arr.pop()
    
    #not pick
    fprint(ind+1, n,arr,nums)


if __name__== "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    arr = []
    fprint(0,n,arr,nums)

# def printS(ind,curr_sum,target,ds,arr):
#     if ind >= len(arr):
#         if curr_sum == target:
#             print(ds)
#         return
    
#     #pick
    
#     ds.append(arr[ind])
#     curr_sum += arr[ind]
#     printS(ind+1,curr_sum,target,ds,arr)

#     curr_sum -= arr[ind]
#     ds.pop()
#     printS(ind+1,curr_sum,target,ds,arr)

# if __name__ == "__main__":
#     print("Target : ", end="")
#     target = int(input())
#     print("arr : ", end="")
#     arr = list(map(int, input().split()))
#     ds = []
#     printS(0,0,target,ds,arr)

