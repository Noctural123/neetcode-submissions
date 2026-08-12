class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupedMap = defaultdict(list)

        for string in strs:
            sortedStr = "".join(sorted(string))
            groupedMap[sortedStr].append(string)

        return groupedMap.values()