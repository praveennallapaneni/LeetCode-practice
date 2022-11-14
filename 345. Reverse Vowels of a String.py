class Solution:
    def reverseVowels(self, s: str) -> str:

        dic = { 'a':1, 'e':2, 'i':3, 'o':4, 'u':5, 'A':6, 'E':7, 'I':8, 'O':9, 'U':10 }
        s = list(s)
        l =0
        r = len(s)-1

        while l<r:
            if s[l] in dic and s[r] in dic:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in dic:
                l += 1
            
            elif s[r] not in dic:
                r -= 1
        
        return ''.join(s)
