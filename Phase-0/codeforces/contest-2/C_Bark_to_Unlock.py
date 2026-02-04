s = input()
n = int(input())

arr = [(input()) for _ in range(n)]

sum = ""
for i in range(n):
    sum += arr[i]
    for j in range(n):
        sum += arr[i]+ arr[j]

if s in sum:
    print("YES")
else:
    print("NO")
    


