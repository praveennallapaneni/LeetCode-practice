class Solution:
    def reverse(self, x: int) -> int:     
        res = 0
        z = abs(x)
        
        while z!=0:
            y = z%10
            res = res *10 + y
            z = z//10
       
        if -2**31 <= res <= (2**31)-1:
            if x>0:
                res = res
            else: 
                res =  -res
            return res
        return 0
