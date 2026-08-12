class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, occur in freq.items():
            bucket[occur].append(num)

        res = []

        for i in range(len(bucket)-1, -1, -1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return res
        
