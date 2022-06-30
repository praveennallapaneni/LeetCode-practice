class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        j_map = {}
        jewel = 0
        for i in jewels:
            j_map[i]=1
        
        for i in range(len(stones)):
            if stones[i] in j_map:
                jewel+=1
        
        return jewel
