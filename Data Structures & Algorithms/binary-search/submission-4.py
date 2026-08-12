class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binary_search(l, r, nums):
            if l > r:
                return -1
            
            mid = (l + r) // 2

            if nums[mid] < target:
                return binary_search(mid+1, r, nums)
            elif nums[mid] > target:
                return binary_search(l, mid-1, nums)
            else:
                return mid

        return binary_search(0, len(nums)-1, nums)