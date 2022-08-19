class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        res = []
        temp = 0
        
        for i in range(len(num)):
            temp = temp*10 + num[i]
        
        temp += k
        temp = str(temp)
        for i in range(len(temp)):
            res.append(int(temp[i]))
        
        return res
