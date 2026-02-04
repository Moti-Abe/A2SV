#problem B. Soldier and Bananas
#link: https://codeforces.com/gym/666791/problem/B

a, b, c = map(int, input().split())
sum = 0
for i in range (c):
    sum += (i+1)*a
if sum > b:
    print(sum-b)
else:
    print(0)