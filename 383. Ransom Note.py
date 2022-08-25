class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hashset = {}
        
        for i in range(len(magazine)):
            if magazine[i] in hashset:
                hashset[magazine[i]] += 1
            
            else:
                hashset[magazine[i]] = 1
                
        for i in range(len(ransomNote)):
            if ransomNote[i] in hashset:
                hashset[ransomNote[i]] -= 1
                
                if hashset[ransomNote[i]] == 0:
                    hashset.pop(ransomNote[i])
                
            else:
                return False
        
        return True
