class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list)

        for string in strs:
            s= ''.join(sorted(string))
            print(s)
            groups[s].append(string)

        return [val for val in groups.values()]