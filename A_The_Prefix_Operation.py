import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for case in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2
    s = data[index]
    index += 1
    
    # Count current number of B's
    current_b = s.count('B')
    
    if current_b == k:
        print(0)
        continue
    
    # Compute suffix B counts: suf[i] = number of B's in positions i to n (1-based)
    suf = [0] * (n + 2)
    for i in range(n, 0, -1):
        suf[i] = suf[i + 1] + (1 if s[i - 1] == 'B' else 0)
    
    # Find the smallest i that works (any valid operation is accepted)
    found = False
    for i in range(1, n + 1):
        suffix_b = suf[i + 1]
        # Try setting prefix i to 'A'
        if suffix_b == k:
            print(1)
            print(i, 'A')
            found = True
            break
        # Try setting prefix i to 'B'
        if i + suffix_b == k:
            print(1)
            print(i, 'B')
            found = True
            break
    
    # The proof guarantees we will always find an i (every k is reachable in 0 or 1 operation)
    # No need for else clause