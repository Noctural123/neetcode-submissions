class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        store = set()
        l = 0

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            
            store.add(s[r])
            longest_substring = max(longest_substring, r-l+1)

        return longest_substring