class Solution:
    def isAnagram(self, s: str, t: str) -> dict:
        
        sdic = {}
        tdic = {}
        
        for i in s:
            if i in sdic:
                sdic[i]+=1
            else:
                sdic[i]=1
        
        for i in t:
            if i in sdic:
                if sdic[i]==1:
                    sdic.pop(i)
                else:
                    sdic[i] -= 1
            else:
                tdic[i]=1
        
        return len(sdic)==0 and len(tdic)==0
