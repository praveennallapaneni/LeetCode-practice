class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        res = []
        item = 0
        
        #saving the values in temp 1-d array
        for i in mat:
            for j in i:
                temp.append(j)

        if len(temp) != r * c:
            return mat
        else: 
            for i in range(r):
                trow = [] #Saving the rows of length c, to append to the res matrix
                for j in range(c):
                    trow.append(temp[item])
                    item += 1
                res.append(trow)
        
        return res
            
        
