class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split() # splits each word in the string into a list
        
        for word in range(len(s)):
            
            s[word] =  s[word][::-1] #reversing each word
        
        return ' '.join(s)  #joining all the words from list
