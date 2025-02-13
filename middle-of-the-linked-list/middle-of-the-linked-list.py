# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Return the middle node, which is now the head of the new list
        return slow
# Function to print the linked list from a given node
    def print_list(head: ListNode):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
            
            print("None")


        