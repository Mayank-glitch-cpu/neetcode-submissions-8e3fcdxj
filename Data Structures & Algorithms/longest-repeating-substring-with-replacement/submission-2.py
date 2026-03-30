class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        result=0
        max_count= 0
        counts= defaultdict(int)
        left=0
        max_count=0

        for right in range(len(s)):
            counts[s[right]]+=1
            max_count= max(max_count, counts[s[right]])

            # if we reached the end and still need more replacements than k 
            while (right-left +1) - max_count> k:
                counts[s[left]]-=1
                left+=1

            result= max(result, right-left+1)

        return result
