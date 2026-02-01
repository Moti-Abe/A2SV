n = int(input())
arr = list(map(int, input().split()))

dict1 = {}

for i,num in enumerate(arr):
    dict1[num] = i+1

for i in range(n):
    print(dict1[i+1], end=" ")