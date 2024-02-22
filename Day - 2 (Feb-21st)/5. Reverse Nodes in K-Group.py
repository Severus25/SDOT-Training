# Leetcode - 25
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        
        # Reverse the current group
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Recursively reverse the remaining groups
        head.next = self.reverseKGroup(curr, k)
        
        return prev
