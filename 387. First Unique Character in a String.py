class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_map = {}
        
        for k in s:        
            if k not in dict_map:
                dict_map[k] = 1  
            else:
                dict_map[k]+=1
                
        for i in range(len(s)):
            if dict_map[s[i]]==1:
                return i
        return -1
