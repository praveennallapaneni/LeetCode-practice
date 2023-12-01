class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0,0

        while i<len(s) and j <len(t):
            if s[i] == t[j]:   # iterating through length of s
                i += 1         # if subsequence exists i will be length of s
            
            j += 1

        return i == len(s)         
