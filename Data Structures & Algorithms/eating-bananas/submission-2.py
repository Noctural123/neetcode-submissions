class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            mid = (l + r)//2
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / mid)
            
            if hours_needed > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
            
        return res