class Solution:
    def climbStairs(self, n: int) -> int:
        
        climb = {1:1, 2:2}
        
        for i in range(3,n+1):
            climb[i]= climb[i-1]+climb[i-2]
        
        return climb[n]
        
