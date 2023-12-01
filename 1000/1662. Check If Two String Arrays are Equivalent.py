class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        str1 = ''
        str2 = ''
        for word in word1:
            for c in word:
                str1 += c 
        for word in word2:
            for c in word:
                str2 += c 

       # str1 = ''.join(word1) # joins all words in to one string
       # str2 = ''.join(word2)


        return str1==str2
