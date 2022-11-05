class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast, temp = 0,0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:

                while temp!=fast:
                    fast = nums[fast]
                    temp = nums[temp]
                
                return temp
