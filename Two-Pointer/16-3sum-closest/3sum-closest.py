class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                add = nums[i] + nums[left] + nums[right]
                if(add < target):
                    if (abs(add - target) < abs(close - target)):
                        close = add
                    left += 1
                elif add > target:
                    if (abs(add - target) < abs(close - target)):
                        close = add
                    right -= 1
                else:
                    return add
        return close
        