import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps= collections.defaultdict(list)

        for string in strs:
            s= ''.join(sorted(string))
            grps[s].append(string)

        return [s for s in grps.values()]