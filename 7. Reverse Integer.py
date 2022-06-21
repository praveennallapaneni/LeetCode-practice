class Solution:
    def reverse(self, x: int) -> int:     
        res = 0
        temp = []
        z = abs(x)
        
        while z!=0:
            y = z%10
            z = z//10
            temp.append(y)
            
        for i in range(len(temp)):
            res = res *10 + temp[i]   
        
    
        if x>0:
            res = res
        else: 
            res =  -res
            
        if -2**31 <= res <= (2**31)-1:
            return res
        else:
            return 0
