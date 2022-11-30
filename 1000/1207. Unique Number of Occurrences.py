class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dic = {}
        res = {}

        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] += 1
            
            else:
                dic[arr[i]] = 1
        
        for j in dic:
            if dic[j] in res:
                return False
            
            else:
                res[dic[j]] = 1
        
        return True
