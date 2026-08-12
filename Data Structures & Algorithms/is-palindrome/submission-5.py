class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        rawString = ""

        for c in s:
            if c.isalnum():
                rawString += c.lower()
        
        return rawString == rawString[::-1]
        
        
