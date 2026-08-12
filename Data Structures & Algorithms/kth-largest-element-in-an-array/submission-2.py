class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

        # Gets the k largest elements in nums and return the smallest one (last elemnent)

        # Ex: [3,2,1,4,5] k = 2
        # heap = [5, 4, 3]
        # Returns 3