class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = dict(collections.Counter(sentence))
        
        if len(dic)==26:
            return True
        
        return False
