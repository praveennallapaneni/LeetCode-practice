class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        res = 0      
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in t:
            if i in dic:
                dic[i] -= 1
                if dic[i]==0:
                    dic.pop(i)      
            else:
                res += 1
        
        return res
