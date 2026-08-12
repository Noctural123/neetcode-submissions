class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temperature, index_of_start]

        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append([temperature, idx])
        
        return res

        # Time: O(n)
        # Space: O(n)

        # [30, 38, 30, 36, 35, 40, 28]


        # curr_temp: 40

        # 35
        # 36
        # 38
        # stack
        
    