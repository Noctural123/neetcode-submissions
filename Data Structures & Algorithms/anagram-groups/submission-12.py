class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))
            hm[sorted_str].append(string)
        
        return list(hm.values())