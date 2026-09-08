# 📖 Problem
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# 💻
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Explanation:

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        tail = dummy

        while tail.next and tail.next.next:
            first = tail.next
            second = first.next

            tail.next = second
            first.next = second.next
            second.next = first

            tail = first

        return dummy.next