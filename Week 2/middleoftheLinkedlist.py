#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.

#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]

#Example 2:
#Input: head = [1,2,3,4,5,6]
#Output: [4,5,6]

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while head:
            #We put nodes in array 
            arr.append(head)
            head = head.next
        return arr[ceil(len(arr)/2)]