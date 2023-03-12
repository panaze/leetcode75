def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        #Create a dictionary
        dictionary = {}    

        #Iterate through linked list
        while head:
            #If node has been already added to the dictionary we have a cycle
            if head in dictionary:
                return True
            
            #If not we add it to the dictionary
            dictionary[head] = True

            #We move through the linked list
            head = head.next
        
        return False