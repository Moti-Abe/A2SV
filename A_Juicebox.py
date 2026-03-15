t = int(input())

while t > 0:
    t -= 1
    n,k = map(int, input().split())

    output = {}
    res = 0
    for i in range(k):
        b, c = map(int, input().split())
        output[b] = output.get(b, 0) + c
    sorted_output = dict(sorted(output.items(), key=lambda x:x[1], reverse=True))

    
    
    count = 0
    for key, value in sorted_output.items():
        res += value
        count += 1
        if count == n:
            break
    
    print(res)

