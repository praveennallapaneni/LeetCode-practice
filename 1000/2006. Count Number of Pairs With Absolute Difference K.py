# time - O(n*n) # space  - O(1) 

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
      output = 0
      for i in range(len(nums)):
        for j in range(i+1,len(nums)):
          if abs(nums[i]-nums[j])==k:
            output+=1
      return output
