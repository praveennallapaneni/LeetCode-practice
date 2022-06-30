class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for i in sentence:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
                
        if len(dic)==26:
            return True
        
        return False
