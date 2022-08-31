class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        res = []
        dic = {}
        a = sorted(list(set(arr)))
        rank = 1

        for i in a:
            dic[i] = rank
            rank += 1
        
        for i in arr:
            res.append(dic[i])
            
        return res
