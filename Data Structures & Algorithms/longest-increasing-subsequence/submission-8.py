class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    temp = max(dp)
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

        # Time: O(n^2) - For each dp valu we're checking all the ones after it
        # Space: O(n) - size of dp