class Solution:
    def sortSentence(self, s: str) -> dict:
        
        res = []
        dic = {}
        
        s = s.split()
        
        for word in range(len(s)):
            dic[int(s[word][-1])] = s[word][0:len(s[word])-1]
        
        for i in range(1,(len(s)+1)):
            res.append(dic[i])
                 
        return ' '.join(res)
