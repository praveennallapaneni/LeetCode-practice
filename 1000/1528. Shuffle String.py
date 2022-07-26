class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        dic = {}
        res = []
        k = 0
        for i in indices:
            dic[i] =  s[k]
            k+=1
            
        for i in range(len(s)):
            res.append(dic[i])
        
        return ''.join(res)
