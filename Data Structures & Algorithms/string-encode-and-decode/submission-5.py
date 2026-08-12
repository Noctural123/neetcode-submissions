class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
    
        for string in strs:
            res += str(len(string)) + "#" + string

        return res


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j




        return res




        # We want:


        # 4#neet4#code4#love3#you
        # 2#we3#say1#:3#yes10#!@#$%^&*()

        # It will always decode correctly since the number will know how many steps to go after the "#"
