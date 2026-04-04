class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        arr = [0] * len(nums)
        pointer = right
        while left <= right:
            ls = nums[left] * nums[left]
            rs = nums[right] * nums[right]
            if ls < rs:
                arr[pointer] = rs
                pointer -= 1
                right -= 1
            else:
                arr[pointer] = ls
                pointer -= 1
                left += 1
        return arr
        