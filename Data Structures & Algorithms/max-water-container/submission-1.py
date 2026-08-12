class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len( heights ) - 1
        maxArea = -float( 'inf' )    
        while lp < rp:
            currArea = self.calArea( lp, rp, heights )
            maxArea = max( maxArea, currArea )

            if heights[ lp ] > heights[ rp ]:
                rp -= 1
                
            elif heights[ lp ] < heights[ rp ]:
                lp += 1

            elif heights[ lp ] == heights[ rp ]:
                lp += 1
        
        return int( maxArea )

    def calArea( self, lp, rp, heights ):
        length = rp - lp
        height = min( heights[ lp ], heights[ rp ] )  
        return length * height