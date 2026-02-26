import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n, x = map(int, input().split())
    
    s = input().strip()
    
    left_walls = s[:x-1].count('#')
    right_walls = s[x:].count('#')
    
    if left_walls == 0 and right_walls == 0:
        ans = 1
        
    elif left_walls > 0 and right_walls > 0:
        right_escape_idx = x + s[x:].find('#') + 1
        left_escape_idx = s[:x-1].rfind('#') + 1
        ans = max(min(x, n - right_escape_idx + 2), min(left_escape_idx + 1, n - x + 1))
        
    elif left_walls == 0 and right_walls > 0:
        right_escape_idx = x + s[x:].find('#') + 1
        ans = min(x, n - right_escape_idx + 2)
        
    else:
        left_escape_idx = s[:x-1].rfind('#') + 1
        ans = min(left_escape_idx + 1, n - x + 1)
        
    output.append(str(ans))
    
    
print('\n'.join(output))