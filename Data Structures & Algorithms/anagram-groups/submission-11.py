class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for string in strs:
            sortedStr = "".join(sorted(string))
            res[sortedStr].append(string)
        
        return list(res.values())