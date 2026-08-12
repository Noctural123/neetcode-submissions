class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for num in nums:
            if num-1 not in numSet:
                length = 1
                while (num+1) in numSet:
                    length+=1
                    num+=1
                longestSeq = max(longestSeq, length)

        return longestSeq