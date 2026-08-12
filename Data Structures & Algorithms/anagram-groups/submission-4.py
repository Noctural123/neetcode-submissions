class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for str in strs:
            sortedStr = ''.join(sorted(str))
            res[sortedStr].append(str)
        
        return list(res.values())