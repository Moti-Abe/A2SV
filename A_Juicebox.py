import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    arr = []
    for _ in range(k):
        brand, cost = map(int, input().split())
        arr.append((brand,cost))

    arr.sort()
    brandMap = {}
    for brand, cost in arr:
        brandMap[brand] = brandMap.get(brand, 0) + cost
    
    values = sorted(brandMap.values(), reverse=True)
    
    if len(values) < n:
        print(sum(values))
    else:
        print(sum(values[0:n]))
    

# import sys 
# from collections import Counter

# input = sys.stdin.readline

# t = int(input())
# output = []
# for _ in range(t):
#     n, k = map(int, input().split())
#     arr = []
#     for _ in range(k):
#         b, c = map(int, input().split())
#         arr.append((b, c))
        
#     arr.sort()
#     counter = Counter()
#     for b, c in arr:
#         counter[b] += c
        
#     vals = sorted(counter.values(), reverse=True)
    
#     max_amount = 0
#     min_len = min(n, len(vals))
#     for i in range(min_len):
#         max_amount += vals[i]
        
#     output.append(str(max_amount))
    
# print('\n'.join(output))
    