class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        
        # Return false if len of array is less than 3
        # check if the array is aligned one side
        
        if n<3 or arr[0]>arr[1] or arr[n-1]>arr[n-2]:
            return False
        
        # 
        i = 1
        while arr[i-1]<arr[i]:
            i+=1
        
        while i < n and arr[i-1]>arr[i]:
            i+=1
        
        return i==n
