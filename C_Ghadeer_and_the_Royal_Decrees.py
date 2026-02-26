t = int(input())

while t > 0:
    t -= 1
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    max_val = max(arr)
    while m > 0:
        m -= 1
        a,b,c = input().split()
        b = int(b)
        c = int(c)
        if b <= max_val <= c:
            if a == "+":
                max_val += 1
            elif a == "-":
                max_val -= 1
        print(max_val, end=" ")
    print()
