class Solution:
    def __init__(self):
        self.empty_string = "<EMP_STR>"
        self.sep = "<SEP>"

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for string in strs:
            if not string:
                new_string += self.empty_string
            else:
                new_string += string
            new_string += self.sep
        if new_string:
            new_string = new_string[:-5]
        return new_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strings = s.split(self.sep)
        for i in range(len(strings)):
            if strings[i] == self.empty_string:
                strings[i] = ""
        return strings