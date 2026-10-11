class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sleft = 0
        tleft = 0
        sright = len(s)
        tright = len(t) 
        if s == '':
            return True
        if t == '':
            return False
        while tleft < tright:
            if s[sleft] == t[tleft]:
                sleft+=1
            tleft+=1
            if sleft == sright:
                return True
        return False
        