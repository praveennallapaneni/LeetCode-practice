class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        a = len(s1)
        b = len(s2)
        
        window = {}
        a_dict = {}
        
        if a>b:
            return False
        
        for i in s1:
            if i in a_dict:
                a_dict[i] += 1
            else:
                a_dict[i] = 1
        
        for i in range(0,a):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1
        
        if window == a_dict:
            return True
        
        
        for i in range(1, b-a+1):
            
            prev = s2[i-1]
            
            if prev in window:
                window[prev] -= 1
                if window[prev] == 0:
                    window.pop(prev)
                    
            nxt = s2[i+a-1]
            
            if nxt in window:
                window[nxt] += 1
            
            else:
                window[nxt] = 1
            
            if window == a_dict:
                return True
        
        return False
