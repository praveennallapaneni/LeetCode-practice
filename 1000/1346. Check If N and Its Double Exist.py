class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(2*arr[i])!=i:
                return True
        return False
