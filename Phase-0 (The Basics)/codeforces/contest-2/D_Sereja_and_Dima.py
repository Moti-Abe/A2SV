n = int(input())

arr = list(map(int , input().split()))

l, r = 0 , n-1
siraj = 0
dima = 0
while l<r:
    if arr[l] > arr[r]:
        siraj += arr[l]
        l += 1 
    else:
        siraj += arr[r]
        r -= 1

    if arr[l] > arr[r]:
        dima += arr[l]
        l += 1
    else:
        dima += arr[r]
        r -= 1
if l == r:
    siraj += arr[l]

print(siraj, end=" ")
print(dima)


    

    
    