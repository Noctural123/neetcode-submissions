class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height)-1

        maxHeightOnRight = []
        maxHeightOnLeft = []

        currLeftMin = float('-inf')
        while l < len(height):
            currLeftMin = max(currLeftMin, height[l])
            maxHeightOnLeft.append(currLeftMin)
            l+=1
        
        currRightMin = float('-inf')
        while r >= 0:
            currRightMin = max(currRightMin, height[r])
            maxHeightOnRight.insert(0, currRightMin)
            r-=1

        # while l < len(height):
        #     maxHeightOnRight.append(max(height[l:]))
        #     l+=1
        
        # while r > 0:
        #     maxHeightOnLeft.insert(0, max(height[:r]))
        #     r-=1

        sum = 0

        for i in range(len(height)):
            sum += min(maxHeightOnLeft[i], maxHeightOnRight[i]) - height[i]
        
        return sum