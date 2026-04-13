class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l,r = 0, 0
        arr = [] # To track  diff between max and min element in the valid sub arr
        max_len = 0
        while r < len(nums):
            arr.append(nums[r])
            if max(arr) - min(arr) <= limit:
                max_len = max(max_len, r-l+1)
                
            else:
                del arr[0]
                l += 1
            r += 1

        return max_len