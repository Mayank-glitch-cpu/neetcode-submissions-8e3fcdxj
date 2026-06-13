class Solution:

    def find_lower(self, arr, target):
        """
        This fucntion takes 
            arr : list / array
            target: int --> find the index to replce the target with
        """
        left, right = 0, len(arr) 

        while left < right:
            mid = (left + right) // 2 

            if arr[mid] < target:
                left = mid +1
            else:
                right = mid
        return left

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x:(x[0], -x[1]))
        # print(envelopes)
        LIS= []

        for w, h in envelopes:
            idx = self.find_lower(LIS, h)

            if idx == len(LIS):
                LIS.append(h)
            else:
                LIS[idx] = h
        return len(LIS)