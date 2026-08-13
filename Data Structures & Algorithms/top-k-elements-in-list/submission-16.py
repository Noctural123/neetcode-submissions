class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, occur in freq.items():
            bucket[occur].append(num)

        res = []

        for arr in reversed(bucket):
            for val in arr:
                res.append(val)
                if len(res) == k:
                    return res
        
        
