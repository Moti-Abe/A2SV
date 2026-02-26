t = int(input())

while t > 0:
    t -= 1
    x = list(map(int, input()))
    
    if len(x) == 1 or sum(x) <= 9:
        print(0)
        continue

    total = sum(x)
    count = 0

    while total > 9:
        mx = max(x)
        ind = x.index(mx)

        if ind == 0:
            reduction = x[0] - 1
            x[0] = 1
        else:
            reduction = x[ind]
            x[ind] = 0

        total -= reduction
        count += 1

    print(count)