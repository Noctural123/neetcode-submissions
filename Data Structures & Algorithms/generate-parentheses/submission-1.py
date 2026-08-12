class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3 Conditions:

        # 1. open == open_c == closed_c -> append joined stack to res, return
        # 2. open_c < n -> backtrack, +1 to open count
        # 3. closed_c < open_c -> backtrack, +1 to closed_count
        stack = []
        res = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()
            
            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

    



    # n = 3
    # 3 open, 3 close
    # close < open