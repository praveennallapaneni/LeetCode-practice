class Solution:
    def balancedStringSplit(self, s: str) -> int:

        res,temp = 0,0
        
        for r in range(len(s)):
            if s[r] == 'R':
                temp += 1
            else:
                temp -= 1
            
            if temp == 0:
                res += 1
                
        return res
