class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq= {}
        current_max= 0
        result= 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) +1
            current_max= max(current_max, freq[s[right]])
            print(freq)
            while (right - left + 1) - current_max > k:
                freq[s[left]] = freq.get(s[left]) - 1
                left += 1

            result = max(result, right - left +1)
        return result 