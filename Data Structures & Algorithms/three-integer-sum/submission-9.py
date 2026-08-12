class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(1, len(nums)):
            target = nums[i] * -1
            j = 0
            k = len(nums)-1

            while j < i and i < k:
                currSum = nums[j] + nums[k]

                print(str(nums[i]) + " + " + str(nums[j]) + " + " + str(nums[k]) + " = " + str(currSum + nums[i]))

                if(currSum < target):
                    j+=1
                elif(currSum > target):
                    k-=1
                elif(currSum == target):
                    res.add(tuple([nums[j], nums[i], nums[k]]))
                    j+=1
                    k-=1
        
        return list(res)
                




        # [-1, 0, 1, 2, -1, -4]


        # [-4, -1, -1, 0, 1, 2]

        # [-4, -3, -2, -1, 0, 1, 4]

        # -2 < 1







        