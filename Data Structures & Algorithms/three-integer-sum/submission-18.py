class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        

        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
              continue  
        
            l, r = i + 1, len(nums) - 1

            while l < r:
                cur_sum = n + nums[l] + nums[r]

                if cur_sum < 0:
                    l += 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1



        return res