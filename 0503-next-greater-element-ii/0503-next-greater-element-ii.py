class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        n = len(nums)
        nge = [-1]*n

        for i in range (n-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            stack.append(nums[i])
        
        for i in range (n):
            if nums[i] > nums[-1]:
                nge[-1] = nums[i]
                break
        return nge