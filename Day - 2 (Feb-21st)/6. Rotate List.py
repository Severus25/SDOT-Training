# Leetcode - 61
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        tail.next = head
        
        k %= length
        
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
