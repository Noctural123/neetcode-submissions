class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''

        for string in strs:
            encodedStr += str(len(string)) +  "#" + string
        
        return encodedStr

    def decode(self, s: str) -> List[str]:

        left = 0
        right = 0
        res = []

        while left < len(s):
            while s[right] != "#":
                right += 1
            
            length = int(s[left:right])
            left = right + 1
            right += 1 + length
            res.append(s[left: right])
            left = right
        
        return res
        
