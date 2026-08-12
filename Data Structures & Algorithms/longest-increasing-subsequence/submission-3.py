class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

                    if dp[i] > max(dp):
                        break
        
        return max(dp)

        # INPUT:
        # nums=[0,1,0,3,2,3]