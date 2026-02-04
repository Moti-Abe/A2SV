# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
mp ={}

for i in range(n):
    key, value = input().split()
    value = int(value)
    mp[key] = (value)
    
import sys

for name in sys.stdin:
    name = name.strip()
    if name in mp:
        print(f"{name}={mp[name]}")
    else:
        print("Not found")
        
