class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        map = {}

        for i in s:
            if i in map:
                map[i] += 1
            
            else:
                map[i] = 1
        
        for i in t:
            if i in map:
                map[i] -= 1
                if map[i] == 0:
                    map.pop(i)

            else:
                return i
