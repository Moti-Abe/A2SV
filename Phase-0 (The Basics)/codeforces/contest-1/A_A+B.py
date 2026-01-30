# Problem A. A+B?
# Link: https://codeforces.com/gym/666791/problem/A

n = int(input())
for _ in range(n):
    expr = input().strip()
    a,b = expr.split('+')
    a = int(a)
    b = int(b)
    print(a+b)
