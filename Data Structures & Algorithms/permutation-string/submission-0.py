class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Freq = {}

        for s in s1:
            s1Freq[s] = s1Freq.get(s, 0) + 1
        
        l = 0

        for r in range(len(s2)):

            if (r - l + 1) == len(s1):
                tempS2 = s2[l:r+1]
                s2Freq = {}
                for s in tempS2:
                    s2Freq[s] = s2Freq.get(s, 0) + 1
                
                if s2Freq == s1Freq:
                    return True
                l += 1
        
        return False

