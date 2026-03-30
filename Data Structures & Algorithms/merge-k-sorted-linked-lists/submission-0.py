# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        # Ensure l1 starts with the smaller value
        if l2.val < l1.val:
            l1, l2 = l2, l1

        head = l1  # This will be the merged head
        while l1 and l2:
            prev = None
            # Advance through l1 as long as its nodes are <= l2
            while l1 and l1.val <= l2.val:
                prev = l1
                l1 = l1.next
            # Now l1 is greater than l2: insert l2 before l1
            prev.next = l2
            # Swap roles: l1 now becomes l2, and we continue
            l1, l2 = l2, l1

        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        n = len(lists)
        interval = 1

        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if n > 0 else None