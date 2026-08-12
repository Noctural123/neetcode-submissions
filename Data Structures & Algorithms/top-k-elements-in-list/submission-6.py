class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        bucket = [[] for i in range(len(nums)+1)]

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        
        for num, freq in freqDict.items():
            bucket[freq].append(num)
        
        bucket.reverse()

        res = []
        for i in range(len(bucket)):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if(len(res) == k):
                    return res
