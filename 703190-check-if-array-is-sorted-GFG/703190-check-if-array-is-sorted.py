class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        left, right = 0,1
        isSorted = True
        while right < len(arr):
            if arr[left] > arr[right]:
                isSorted = False
                break
            left += 1
            right += 1
        
        return isSorted
                