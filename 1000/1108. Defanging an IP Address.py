class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        res= ''
        for i in address:
            if i == '.':
                i ='[.]'
            res+=i
                
        return res
        
