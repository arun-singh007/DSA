class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        if r==0:
            return True
        while l <= r :
            if (('A' <= s[l] <= 'Z' or '0' <= s[l] <= '9') or ('a' <= s[l] <= 'z' or '0' <= s[l] <= '9')) and (('A' <= s[r] <= 'Z' or '0' <= s[r] <= '9') or ('a' <= s[r] <= 'z' or '0' <= s[r] <= '9')):
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l+=1
                    r-=1
            else :
                if l <= r and not(('A' <= s[l] <= 'Z' or '0' <= s[l] <= '9') or ('a' <= s[l] <= 'z' or '0' <= s[l] <= '9'))  :
                    l+=1
                if l <= r and not(('A' <= s[r] <= 'Z' or '0' <= s[r] <= '9') or ('a' <= s[r] <= 'z' or '0' <= s[r] <= '9'))  :
                    r-=1
        return True
        