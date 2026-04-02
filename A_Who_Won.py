t = int(input())
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    if ((x1 > y1 and x2 > y2) and y2 >= x1) or ((x1 < y1 and x2 < y2) and x2 >= y1) or ((x1 < y1) and (x2 >= y1)) or ((x1 > y1) and (y2 >= x1)):
        print("YES")
    else:
        print("NO")
