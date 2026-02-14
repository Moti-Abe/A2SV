t = int(input())

while t > 0:
    t -= 1
    a, b, c = map(int, input().split())

    if a == b + c or b == a+c or c == a + b:
        print("YES")
    else:
        print("NO")
