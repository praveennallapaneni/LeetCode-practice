class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dic = {}
        count = 0
        for i in allowed:
            dic[i]=1
        
        for i in words:
            for j in i:
                if j not in dic:
                    count+=1
                    break
        return len(words)-count
