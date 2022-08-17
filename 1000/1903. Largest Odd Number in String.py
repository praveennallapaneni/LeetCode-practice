class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        res = 0
        
        if int(num)%2 == 1:
            return num
        
        for i in range(len(num),0,-1):
            num = num[:i]
            
            if int(num[i-1])%2 == 1:
                return num
            
        return ""
