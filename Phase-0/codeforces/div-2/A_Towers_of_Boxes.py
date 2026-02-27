import math
t = int(input())
while t > 0:
    t -= 1
    n, m , d = map(int, input().split())
    tower_len = (d//m) + 1
    if tower_len > n:
        print(1)
    else:
        print(math.ceil(n/tower_len))