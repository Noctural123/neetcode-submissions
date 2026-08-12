class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}

        for i in range(len(nums)):
            if nums[i] in hs:
                return [hs[nums[i]], i]
            
            hs[target-nums[i]] = i
        