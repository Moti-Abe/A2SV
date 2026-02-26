a , b = map(int , input().split())
n = int(input())

fallen = False
for i in range (n):
    c, d = map(int, input().split())
    if a < c or (a == c and b > d):
        fallen = True
        break
          
if fallen:
    print("The Fallen Champion")
else:
    print("The Champion Saves the Accused")