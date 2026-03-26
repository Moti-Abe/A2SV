class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range (1,n):
            nums[i] += nums[i-1]

        for i in range(n-1):
            check = nums[n - 1] - nums[i]
            if check == 0:
                return 0
            ind = nums.index(nums[i]) + 1
            if  check in nums[ind:]:
                return nums.index(check)
        
        return -1

        