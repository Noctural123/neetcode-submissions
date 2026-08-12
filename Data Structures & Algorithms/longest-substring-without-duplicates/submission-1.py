class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        left = 0
        hs = set()

        for right in range(len(s)):
            
            while s[right] in hs:
                hs.remove(s[left])
                left+=1
            hs.add(s[right])
            longestSubstring = max(longestSubstring, right-left+1)
        
        return longestSubstring