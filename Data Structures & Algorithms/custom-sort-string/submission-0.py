class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq= {char: i  for i, char in enumerate(order)}
        return ''.join(sorted(s,key=lambda c: freq.get(c,26)))