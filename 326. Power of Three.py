class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0:
            return False
        elif n == 1:
            return True
        
        return n>0 and 1162261467 % n == 0
