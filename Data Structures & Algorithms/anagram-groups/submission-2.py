class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list)

        for string in strs:
            s= ''.join(sorted(string))
            groups[s].append(string)

        return [val for val in groups.values()]