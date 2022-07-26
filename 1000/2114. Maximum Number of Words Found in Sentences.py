class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maximum = 0
        
        for i in range(len(sentences)):
            
            temp = sentences[i].split()
            l = len(temp)
            
            maximum = max(maximum,l)
        
        return maximum
