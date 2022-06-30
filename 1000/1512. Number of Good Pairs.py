class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        output =0
        dict_map = {}
        
        for i in nums:
            if i in dict_map:
                if dict_map[i]==1:
                    output+=1
                
                else:
                    output+=dict_map[i]
                dict_map[i]+=1
            else:
                dict_map[i]=1
        
        return output
