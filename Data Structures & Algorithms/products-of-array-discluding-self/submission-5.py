class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        res.append(1)
        i = 0

        while len(res) < len(nums):
            res.append(nums[i] * res[i])
            i += 1
        
        curr = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            res[i] *= curr
            curr *= nums[i]

        return res

        # nums = [1,2, 4, 6]

        # res = [1, 1, 2, 8]