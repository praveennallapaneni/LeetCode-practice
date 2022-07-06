class Solution:
    def tribonacci(self, n: int) -> int:
        
        trib = {0:0,1:1,2:1}
        
        for i in range(3,n+1):
            trib[i]= trib[i-1]+trib[i-2]+trib[i-3]
        
        return trib[n]
