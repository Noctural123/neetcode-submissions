class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        compIndex = {}

        for i in range(len(nums)):
            if nums[i] in compIndex:
                return [compIndex[nums[i]], i]
            compIndex[target-nums[i]] = i