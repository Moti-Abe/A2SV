s = "motiabebete"

array_dict = [0]*26

offset = ord('a')

for i in range (len(s)):
    ascii = ord(s[i])

    array_dict[ascii - offset] += 1

print(array_dict)
