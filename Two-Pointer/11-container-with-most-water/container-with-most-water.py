class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            water = abs(right - left) * min(height[left],height[right])
            max_water = max(water,max_water)
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return max_water


        