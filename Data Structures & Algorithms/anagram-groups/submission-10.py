class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedDict = defaultdict(list)

        for string in strs:
            sortedStr = "".join(sorted(string))
            sortedDict[sortedStr].append(string)
        
        return sortedDict.values()