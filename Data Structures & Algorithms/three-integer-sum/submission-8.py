class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index,val in enumerate (nums):
            if val > 0: 
                break
            
            if index > 0 and val == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                currSum = val + nums[left] + nums[right] 

                if currSum < 0:
                    left += 1 
                elif currSum > 0:
                    right -= 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
        
        return res
                







        [-2, -2, 0, 0, 0, 2, 2, 2]

        [-1, 0, 1, 2, -1, -4]

        [-4, -1, -1, 0, 1, 2]