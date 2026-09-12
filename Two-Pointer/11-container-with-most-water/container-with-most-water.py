class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            water = width * min(height[left],height[right])
            if max_water < water:
                max_water = water
            if min(height[left],height[right]) == height[left]:
                left = left + 1
            elif min(height[left],height[right]) == height[right] :
                right = right - 1
            else :
                left = left + 1
                rihgt = right - 1
        return max_water