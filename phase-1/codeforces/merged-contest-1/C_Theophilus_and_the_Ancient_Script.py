t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    s = input()
    if "A" in s and "B" in s:
        ind_a = s.index("A")
        ind_b = s.rindex("B")
        max_swap = (ind_b - ind_a)
        if max_swap >= 0:
            print(max_swap)
        else:
            print(0)
    else:
        print(0)
