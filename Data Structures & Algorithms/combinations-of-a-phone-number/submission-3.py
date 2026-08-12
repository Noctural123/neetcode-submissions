class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            for char in digit_to_char[digits[i]]:
                dfs(i+1, curr_str + char)
        
        dfs(0, "")
        return res if res[0] else []


        

        # digits = "34"

        # i = 1
        # curr_str = "eh" -> so on

        # res = ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fg", "fi"]