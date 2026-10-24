class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        left = 0
        right = len(nums) - 1
        nums.sort()
        res = []
        while left < right - 1:
            left_itr = left + 1
            right_itr = right
            while left_itr < right_itr:
                add = nums[left] + nums[left_itr] + nums[right_itr]
                if add == 0:
                    res.append([nums[left], nums[left_itr], nums[right_itr]])
                    while left_itr+1 < right_itr and nums[left_itr] == nums[left_itr+1]:
                        left_itr+=1
                    while right_itr - 1 > left_itr and nums[right_itr] == nums[right_itr-1]:
                        right_itr-=1
                    right_itr-=1
                    left_itr+=1
                elif add > 0:
                    right_itr-=1
                else:
                    left_itr+=1
            while left+1 < len(nums) and nums[left] == nums[left+1]:
                left+=1
            left+=1
        return res

        