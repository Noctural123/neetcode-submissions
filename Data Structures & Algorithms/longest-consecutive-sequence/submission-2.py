class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in nums:
            currCount = 0
            if num-1 not in numSet:
                startingNum = num
                currCount = 1
                while num+1 in numSet:
                    currCount += 1
                    num += 1
            
            longest = max(longest, currCount)
        
        return longest



