class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        s = 0        
        length = len(mat[0])
        i = 0 
        j = length-1
        
        while length > 0:
            
            if i != j:
                s = s + mat[i][i] + mat[i][j]
            else:
                s = s + mat[i][i]
            i+=1
            j-=1
            length -=1
                     
        return s
