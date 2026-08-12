class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1
        volume = 0

        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                volume += leftMax - height[l]
                print("leftMax: " + str(leftMax))
                print(volume)
            else:
                r -=1
                rightMax = max(rightMax, height[r])
                volume += rightMax - height[r]

        return volume


