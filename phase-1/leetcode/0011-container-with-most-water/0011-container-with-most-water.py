class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        max_area = 0
        while left < right:
            min_hight = min(height[left], height[right])
            width = right - left
            area = min_hight*width
            max_area = max(max_area, area)
            if min(height[left+1], right) > min(height[right-1],left):
                left += 1
            else:
                right -= 1
        return max_area

