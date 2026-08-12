class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            res += self.palindrome_count(l, r, s)
            
            # even length
            l, r = i, i + 1
            res += self.palindrome_count(l, r, s)
        
        return res
    
    def palindrome_count(self, l, r, s):
        count = 0
        while l >= 0 and r < len(s) and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1
        
        return count