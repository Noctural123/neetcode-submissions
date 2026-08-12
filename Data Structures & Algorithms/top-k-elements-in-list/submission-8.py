class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        for val, frequency in freq.items():
            bucket[frequency].append(val)
        
        bucket.reverse()
        res = []
    
        for item in bucket:
            for val in item:
                res.append(val)
                if len(res) == k:
                    return res