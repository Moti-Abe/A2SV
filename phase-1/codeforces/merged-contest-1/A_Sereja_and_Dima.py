n = int(input())
arr = list(map(int, input().split()))

left , right = 0, n-1

sirja, dima = 0, 0

while left < right:
    if arr[left] > arr[right]:
        sirja += arr[left]
        left += 1
    else:
        sirja += arr[right]
        right -= 1
    
    
    if arr[left] > arr[right]:
        dima += arr[left]
        left += 1
    else:
        dima += arr[right]
        right -= 1

if n%2 != 0:
    sirja += arr[left]

print(sirja,end=" ")
print(dima)

