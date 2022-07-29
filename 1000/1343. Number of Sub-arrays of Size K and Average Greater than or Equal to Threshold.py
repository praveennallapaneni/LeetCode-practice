class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        runSum = sum(arr[0:k])
        avg = float(runSum//k)
        
        res = 0
        
        if avg >= threshold:
            res = 1
        
        for i in range(len(arr)-k):
            runSum += arr[i+k] - arr[i]
            
            avg = float(runSum//k)
            
            if avg >= threshold:
                res += 1
        
        return res
