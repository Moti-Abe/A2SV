#problem E. Only Pluses
#link: https://codeforces.com/gym/666791/problem/E

t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    for i in range(5):
        if a <= b and a <= c:
            a += 1
        elif b <= a and b <= c:
            b += 1
        elif c <= a and c <= b:
            c += 1
        
    print(a*b*c)
