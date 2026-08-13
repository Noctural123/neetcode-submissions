class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]
        
        for i in range(len(nums) - 1):
            res.append(res[i] * nums[i])

        curr_num = nums[-1]

        for i in range(len(res) - 2, -1, -1):
            res[i] *= curr_num
            curr_num *= nums[i]

        return res

        # nums = [1, 2, 4, 6]
       
        # res = [1, 1, 12, 8]
        