class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        if len(s)<3:
            return 0
        
        window = {}
        res = 0
        
        if len(s) >= 3:
            
            for i in range(0, 3):
                if s[i] not in window:
                    window[s[i]] = 1
                
                else:
                    window[s[i]] += 1
                    
        if len(window) == 3:
            res = 1
        
        for i in range(3,len(s)):
            
            prev = s[i-3]
            
            if s[i-3] in window:
                window[s[i-3]] -= 1
                if window[s[i-3]] == 0:
                    window.pop(s[i-3])
            
            nxt = s[i]
            
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
            
            if len(window) == 3:
                res += 1
        
        return res
        
