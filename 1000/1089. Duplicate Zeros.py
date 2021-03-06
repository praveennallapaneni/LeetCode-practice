# Using Python Functions

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.insert(i+1, 0) 
                arr.pop()
                i += 2
            else:
                i += 1


# Adding new values to array
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = arr.count(0)
        
        l = len(arr)-1
        nl = len(arr)-1+zeros
        
        while l < nl:
            if nl<len(arr):
                arr[nl] = arr[l]
            
            if arr[l]==0:
                nl-=1
                if nl <len(arr):
                    arr[nl]=0
            
            l-=1
            nl-=1
