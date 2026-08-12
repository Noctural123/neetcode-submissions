class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        compIndexDict = {}

        for i, num in enumerate(nums):

            if num in compIndexDict:
                return [compIndexDict[num], i]
            
            compIndexDict[target-num] = i