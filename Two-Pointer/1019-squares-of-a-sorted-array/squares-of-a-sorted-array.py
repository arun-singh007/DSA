class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * (r+1)
        flag=r
        # if len(nums) == 1:
        #     nums[0] = nums[0] ** 2
        #     return nums
        while l <= r:
            lsqr = nums[l] ** 2
            rsqr = nums[r] ** 2
            if rsqr > lsqr:
                res[flag] = rsqr
                r-=1
            else:
                res[flag]=lsqr
                l+=1
            flag-=1
        return res
        