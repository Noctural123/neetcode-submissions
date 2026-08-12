class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            curr_total = 0
            for pile in piles:
                curr_total += math.ceil(pile / mid)
            
            if curr_total > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        
        return res