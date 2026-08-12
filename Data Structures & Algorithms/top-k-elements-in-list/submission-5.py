class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freqList = [[] for i in range (len(nums)+1)]
        
        for i in range(len(nums)):
            hmap[nums[i]] = hmap.get(nums[i], 0) + 1

        for val, freq in hmap.items():
            freqList[freq].append(val)

        res = []
        for item in reversed(freqList):
            for val in item:
                res.append(val)
                if(len(res) == k):
                    return res
        return res