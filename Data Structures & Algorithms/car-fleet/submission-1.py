class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = [] # time_taken

        for p, s in sorted(pair)[::-1]:
            time_taken = (target - p) / s
            stack.append(time_taken)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



# Time: O(n log n) = Sorting
# Space: O(n)
