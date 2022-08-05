class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        flag = True
        l = 0
        
        for i in range(0,len(s)):
            if s[i] == ' ':
                flag = True
            
            else:
                if flag == True:
                    l = 1
                    flag = False
                else:
                    l += 1
            
        return l
      
      
#using Split function

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.split()
        
        return len(s[-1])
