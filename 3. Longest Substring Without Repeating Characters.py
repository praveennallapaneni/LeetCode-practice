class Solution:
    def lengthOfLongestSubstring(self, s: str) -> dict:
        
        res = 0
        seen = {}
        l = 0
        
        for i in range(len(s)):
            if s[i] in seen:
                l = max(seen[s[i]],l)
                
            seen[s[i]]=i+1
            
            res = max(res, i-l+1)
        
        return res
