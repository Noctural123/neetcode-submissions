class Solution:
    def trap(self, height: List[int]) -> int:

        leftMax = []
        rightMax = []

        left = 0

        while left < len(height):
            leftMax.append(max(height[left:]))
            left += 1


        right = len(height)

        while right > 0:
            rightMax.insert(0, max(height[:right]))
            right -= 1

        totalWater = 0

        for i, val in enumerate(height):
            totalWater += min(rightMax[i], leftMax[i]) - val
        
        return totalWater



    
            
            



        