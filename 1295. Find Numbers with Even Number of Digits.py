class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for i in range(0,len(nums)):
            j = 0         
            while nums[i]>0:
                nums[i]= nums[i]//10
                j += 1            
            if j%2==0:
                count +=1
        
        return count
