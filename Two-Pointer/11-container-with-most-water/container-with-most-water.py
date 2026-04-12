class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        current_max = 0
        while left < right:
            temp_max = min (height[left] ,height[right]) * (right - left)
            if temp_max > current_max:
                current_max = temp_max
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return current_max
