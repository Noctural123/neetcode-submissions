class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)
        

        for string in strs:
            sortedStr = "".join(sorted(string))
            hmap[sortedStr].append(string)
        
        return hmap.values()