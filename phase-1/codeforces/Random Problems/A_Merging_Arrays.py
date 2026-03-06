n , m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
left , right = 0 , 0

while left < n and right < m:
    if arr1[left] < arr2[right]:
        res.append(arr1[left])
        left += 1
    else:
        res.append(arr2[right])
        right += 1

while left == n and right <  m:
    res.append(arr2[right])
    right += 1

while right == m and left < n:
    res.append(arr1[left])
    left += 1

print (*res)
        

