s = input()
t = input()

vowels = ['a', 'e', 'i','o','u']
ispossible = True
if len(s) != len(t):
    ispossible = False
else: 
    for i in range(len(s)):
        if (s[i] in vowels) != (t[i] in vowels):
            ispossible = False
            break

if ispossible:
    print("Yes")
else:
    print("No")

