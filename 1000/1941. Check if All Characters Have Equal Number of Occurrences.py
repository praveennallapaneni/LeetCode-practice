class Solution:
    def areOccurrencesEqual(self, s: str) -> str:
        
        d = Counter(s).values()
         
        return len(set(d))==1
