# Problem : https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    arr = list(s)
    for i in range(len(arr)):
        if arr[i] == arr[i].lower():
            arr[i] = arr[i].upper()
        else:
            arr[i] = arr[i].lower()
        
    return "".join(arr)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)