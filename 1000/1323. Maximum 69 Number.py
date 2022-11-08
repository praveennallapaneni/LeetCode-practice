class Solution:
    def maximum69Number (self, num: int) -> int:
        
        # replace the first occurance of char 6 with char 9 
        res = str(num).replace('6','9',1)
        
        return int(res)
