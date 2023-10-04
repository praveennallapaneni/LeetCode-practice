class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l1, l2 = 0, 0

        out = ''

        while l1<len(word1) or l2 < len(word2):
            if l1 < len(word1):
                out += word1[l1]

            if l2 < len(word2):
                out += word2[l2]

            l1 +=1
            l2 +=1

        return out
