class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse= True)
        g.sort(reverse = True)
        i,j,res = 0,0,0
        
        while i < len(g) and j <len(s):
            if s[j] >= g[i]:
                res += 1
                j += 1
            i += 1

        return res
