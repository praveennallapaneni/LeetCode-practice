#Brute Force
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        for i in range(1,num+1):
            if i**2 == num:
                return True
            if i**2 > num:
                return False

# Binary Search Method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left = 1
        right = num
        
        while left <= right:
            mid =  left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
