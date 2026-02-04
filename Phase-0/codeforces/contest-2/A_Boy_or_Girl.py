s = input()

st = set()

for i in range (len(s)):
    st.add(s[i])

if len(st)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")