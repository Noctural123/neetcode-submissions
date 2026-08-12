class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, idx]

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append([temp, idx])
        return res