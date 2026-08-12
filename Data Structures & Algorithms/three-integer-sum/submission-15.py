class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(1, len(nums)):
            target = nums[i] * -1
            l, r = 0, len(nums)-1

            while l<i and i<r:
                currSum = nums[l] + nums[r]

                if currSum < target:
                    l+=1
                elif currSum > target:
                    r-=1
                else:
                    res.add(tuple([nums[l], nums[i], nums[r]]))
                    l+=1
                    r-=1

        return list(res)

    



    [-1, 0, 1, 2, -1, -4]

    [-4, -1, -1, 0, 1, 2]
        






        