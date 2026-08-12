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
            maxHeightOnRight.append(currRightMin)
            # Dont use insertion since insertion is O(n) so insertion for n elements => O(n^2) time complexity

            r-=1
        maxHeightOnRight.reverse()

        sum = 0

        for i in range(len(height)):
            sum += min(maxHeightOnLeft[i], maxHeightOnRight[i]) - height[i]
        
        return sum