# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l,r = 1,n 
        
        while l<=r:
            mid = l + (r-l)//2
            
            if isBadVersion(mid) == False :
                l = mid +1
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == True:
                r = mid -1
            else:
                return mid
                
