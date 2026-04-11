t = int(input())
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    if (x1 > y1 and x2 > y2) or (x1 < y1 and x2 < y2) :
        print("YES")
    else:
        print("NO")
