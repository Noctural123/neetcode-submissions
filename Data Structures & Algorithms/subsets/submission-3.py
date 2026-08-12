class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Time: O(2^n * n) -> 2^n subsets with n operations per subset (the copy)
        # Space: O(2^n * n) -> 2^n subsets each subset up to n elements
        subset = []
        res = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

        



#            []
#         /      \
#        1        []
#      /  \       /  \
#     12    1    2    []
#  123 12 13 1  23 2 3  []