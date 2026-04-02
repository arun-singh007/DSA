class Solution:
    def check(self,l,r,s) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        did_not_match = 0
        while left < right:
            if s[left] != s[right]:
                return self.check(left+1,right,s) or self.check(left,right-1,s)
            left += 1
            right -= 1
        return True
    
