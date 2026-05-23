class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1] * len(nums1)
        n1_map= {num:i for i , num in enumerate(nums1)}

        for i in range(len(nums2)):
            if nums2[i] not in n1_map:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = n1_map[nums2[i]]
                    out[idx] = nums2[j]
                    break
        return out