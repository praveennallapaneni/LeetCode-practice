class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        output = []
        dic = {}
        
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        for i in range(len(nums)):
            a = 0
            for j in dic:
                
                if nums[i]>j:
                    for k in range(0,dic[j]):
                        a+=1
            output.append(a)
        
        return output
