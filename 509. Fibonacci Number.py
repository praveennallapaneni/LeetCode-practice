#Recursion 

class Solution:
    def fib(self, n: int) -> int:
        
        if n==0:
            return 0
        if n==1:
            return 1
        
        
        return self.fib(n-1) + self.fib(n-2)
      
  # Iterative
  
  class Solution:
    def fib(self, n: int) -> int:
        
        fibo = { 0:0,1:1}
        
        for i in range(2,n+1):
            fibo[i]= fibo[i-1]+fibo[i-2]
            
        return fibo[n]
