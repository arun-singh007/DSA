class Solution:
    def ispalin(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if not(self.ispalin(s,left+1,right) or self.ispalin(s,left,right-1)):
                    return False
                else:
                    return True
            left+=1
            right-=1
        return True

        