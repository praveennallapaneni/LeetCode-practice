class Solution:
    def minimumSum(self, num: int) -> int:
        temp =[]
        new1, new2 = 0,0
        
        while num>0:
            temp.append(num%10)
            num = num//10
            
        temp.sort()
        
        for i in range(0,len(temp),2):
            new1 = new1*10 + temp[i]
            
        for i in range(1,len(temp),2):
            new2 = new2*10 + temp[i]
            
        return new1+new2
