class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            key = ''.join(sorted(string))
            groups[key].append(string)

        return [value for _, value in groups.items()]