class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, arr, curr_sum):
            if curr_sum == target:
                res.append(arr.copy())
                return
            
            if curr_sum > target or i == len(nums):
                return
            
            arr.append(nums[i])
            dfs(i, arr, curr_sum + nums[i])

            arr.pop()
            dfs(i+1, arr, curr_sum)


        dfs(0, [], 0)
        return res
