class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {'}' : '{',
                     ')' : '(',
                     ']' : '['}
        stack = []


        for p in s:
            if p in paren_map:
                
                if not stack or paren_map[p] != stack.pop():
                    return False
            else:
                stack.append(p)
        
        return not stack
        # ([{}])
        # # stack = (,