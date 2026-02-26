import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n, m = map(int, input().split())
    
    decks = [] 
    for _ in range(n):
        arr = list(map(int, input().split()))
        arr.sort()   
        decks.append(arr)
        
    exists = True
    for arr in decks:
        if not exists:
            break
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != n:
                exists = False
                break
        
    if not exists:
        output.append('-1')
    else:
        order = [(arr[0], i + 1) for i, arr in enumerate(decks)]
        order.sort()
        
        indices = [str(el[1]) for el in order]
        output.append(' '.join(indices))
        
print('\n'.join(output))