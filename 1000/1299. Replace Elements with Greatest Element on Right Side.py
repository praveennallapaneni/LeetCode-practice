class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        temp = arr[-1]
        
        i = len(arr)-1
        while i>=0:
            x = arr[i-1]
            arr[i-1]=max(arr[i],temp)
            temp = x
            i -= 1
        arr[-1]=-1
        return arr
