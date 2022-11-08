class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}

        for i in range (len(names)):
            map[heights[i]] = names[i]
        
        res =[]

        for i in sorted(map.items(),reverse = True):
            res.append(i[1])
        
        return res
