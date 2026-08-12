class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for string in strs:
            encoded_str += str(len(string)) + "#" + string
        return encoded_str

    def decode(self, s: str) -> List[str]:

        l = 0
        r = 0
        res = []

        while l < len(s):
            while s[r] != "#":
                r += 1
            
            length = int(s[l:r])
            l = r + 1
            r += length + 1
            res.append(s[l:r])
            l = r
        
        return res
