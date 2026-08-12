class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res



        # height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

        # l = 3
        # r = 3
        # leftMax = 3
        # rightMax = 3

        # height[l] = 3
        # height[r] = 1

        # res = 9
        



