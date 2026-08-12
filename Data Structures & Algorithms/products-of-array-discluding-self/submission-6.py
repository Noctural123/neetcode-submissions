class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]
        i = 0
        
        while len(res) < len(nums):
            res.append(res[i] * nums[i])
            i += 1

        curr_num = nums[-1]

        for i in range(len(res) - 2, -1, -1):
            res[i] = curr_num * res[i]
            curr_num *= nums[i]

        return res

        # nums = [1, 2, 4, 6]
       
        # res = [48, 24, 12, 8]
        