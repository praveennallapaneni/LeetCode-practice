class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        time = 0
        i = 1
        
        while i < len(points):
            d1 = abs(points[i][0]-points[i-1][0])
            d2 = abs(points[i][1]-points[i-1][1])
            
            time += max(d1,d2)           
            i += 1
        
        return time
