class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        groupedDict = defaultdict(list)

        for string in strs:
            sortedStr = "".join(sorted(string))
            groupedDict[sortedStr].append(string)
        
        return groupedDict.values()