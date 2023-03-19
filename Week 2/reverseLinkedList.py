#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            #We save the next node in a temporary variable
            next_temp = curr.next
            #We reverse the list
            curr.next = prev
            #We make our previous node to be the current node we are in
            prev = curr
            #We make the current node our node 
            curr = next_temp

        return prev

def main():
    print(reverseList([1,2,3,4,5]))

    
# Path: Week 2/reverseLinkedList.py