class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dic = {}
        res = 0
        counter = 0
        
        # converting string to dictionary
        for i in s: 
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        for i in dic:
            if dic[i]%2!=0: # adding odd values
                res += (dic[i]-1)
                counter = 1
            else: # adding even values
                res += dic[i]
            
        if counter == 1:
            res+= 1
        
        return res
