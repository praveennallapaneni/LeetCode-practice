class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res =[[1]]
        
        for i in range(rowIndex):
            temp = [0]+ res[-1]+[0]  #Adding 0's at both ends
            row = []
            for j in range(len(temp)-1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res[-1]
