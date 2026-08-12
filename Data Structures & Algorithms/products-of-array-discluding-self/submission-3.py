class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        res.append(1)
        i = 0

        while len(res) < len(nums):
            res.append(res[i] * nums[i])
            i += 1

        rightProduct = nums[len(nums)-1]

        for i in range(len(nums)-2, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        
        return res