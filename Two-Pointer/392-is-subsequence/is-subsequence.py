class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0
        slen = len(s)
        tlen = len(t)
        if slen == 0 :
            return True
        if tlen == 0 :
            return False
        while sp < slen :
            if s[sp] == t[tp]:
                sp = sp + 1
            tp = tp + 1
            if tp == tlen :
                break
        return sp == slen
        