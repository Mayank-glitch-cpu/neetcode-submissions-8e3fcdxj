class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list)

        for string in strs:
            key= ''.join(sorted(string))
            groups[key].append(string)

        return [val for key, val in groups.items()]
        
