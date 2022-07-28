class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        a = len(s)
        b = len(p)
        res =[]
        window = {}
        pdict = {}
        
        if a<b:
            return res
        
        for i in p:
            if i in pdict:
                pdict[i]+=1
            else:
                pdict[i] = 1
        
        for i in range(0,b):
            if s[i] in window:
                window[s[i]]+=1
            else:
                window[s[i]]=1
                
        if pdict == window:
            res.append(0)
            
        for i in range(1, a-b+1):
            
            last = s[i-1]
            
            if last in window:
                window[last] -=1
                
                if window[last]==0:
                    window.pop(last)
            
            nxt = s[i+b-1]
            
            if nxt in window:
                window[nxt] += 1
            else:
                window[nxt] = 1
            
            if window == pdict:
                res.append(i)

        return res
