class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # KEEP ON MOVING R TO MID WHEN ITS NORMAL, ONCE ITS WEIRD DO L = MID + 1
        while l < r:
            mid = (l + r) // 2

            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]




        # [3, 4, 5, 6, 1, 2]
        # [5, 0, 1, 2, 3, 4]
        #  l     m        r