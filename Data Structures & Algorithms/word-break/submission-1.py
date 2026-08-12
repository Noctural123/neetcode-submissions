class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break

        return dp[0]


        # Time: O(n*m*k)
        # n = length of s
        # m = number of words in wordDict
        # k = average lenght of each word. (s[i : i + len(w)] == w)

        # Space: O(n)
        # dp array of size O(n+1) -> O(n)