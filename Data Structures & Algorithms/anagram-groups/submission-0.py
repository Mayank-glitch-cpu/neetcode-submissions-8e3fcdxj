class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strings= defaultdict(list)
        for string in strs:
            key= ''.join(sorted(string))
            grouped_strings[key].append(string)
        print(grouped_strings)
        return list(grouped_strings.values())