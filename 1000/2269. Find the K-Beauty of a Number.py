class Solution:
    def divisorSubstrings(self, num: int, k: int) -> list:
        
        beauty = 0
        snum = str(num)
        l = len(str(num))
        window = []
        
        for i in range(0,k):
            window.append(snum[i])
            
        if num%int(''.join(window)) == 0:
            beauty = 1
        
        for i in range(k,l):
            window = []
            for j in range(i-k+1,i+1):
                window.append(snum[j])
            
            temp = int(''.join(window))
            
            if temp == 0:
                temp = num + 1
                
            if num% temp == 0:
                beauty += 1
        
        return beauty
