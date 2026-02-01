n = int(input())

s = input()

arr = list(s)

st = set()

for i in range(n):
    arr[i] = arr[i].lower()
    st.add(arr[i])

if len(st) == 26:
    print("YES")
else:
    print("NO")



