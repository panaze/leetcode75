# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(self, list1, list2):
        #Create ListNode that will serve as the final merged List
        pointer = dummy = ListNode()
    
        #Check if list 1 is empty
        if list1 is None:
            return list2
    
        #Check if list 2 is empty
        if list2 is None:
            return list1
        

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next

            pointer = pointer.next


        if list1 or list2:
            if list1:
                pointer.next = list1
            else:
                pointer.next = list2
            
        return dummy.next

def main():
  print(isValid("[]"))

main()