class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0

        left = 0
        right = len(heights)-1

        while left < right:
            minHeight = min(heights[left], heights[right])
            maxWater = max(minHeight * (right-left), maxWater)
            
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
            
        return maxWater
        