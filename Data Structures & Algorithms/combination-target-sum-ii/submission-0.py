class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(candidates)

        res = []

        def dfs(i, curr, total):
            if total == target and curr.copy() not in res:
                res.append(curr.copy())
                return
            
            if i >= len(sorted_nums) or total > target:
                return
            
            curr.append(sorted_nums[i])
            dfs(i+1, curr, total + sorted_nums[i])
            curr.pop()
            dfs(i+1, curr, total)


        dfs(0, [], 0)
        return res