t = int(input())

while t > 0:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    monasters = []
    for i in range(n):
        monasters.append([ abs(x[i]) , a[i] ])
    
    monasters.sort(key=lambda m: m[0])

    total_health = 0

    for i in range(n):
        total_health += monasters[i][1]
        if total_health >  k*monasters[i][0]:
            print("NO")
            break
    else:
        print("YES")
