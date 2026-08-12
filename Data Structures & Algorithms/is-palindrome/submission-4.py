class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        rawString = ""

        for c in s:
            if c.isalnum():
                rawString += c.lower()
        
        reversedRawString = "".join(reversed(rawString))
        return rawString == reversedRawString
        
        
