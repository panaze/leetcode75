def isBalanced(root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(root):
            if root is None:
                    return 0
            left = check(root.left)
            right = check(root.right)

            #If we found a difference of height > 1 in any of      
            #the other levels  
            if left == -1 or right == -1:
                return -1
            #If the difference between left and right subtree is > 1    
            #means it is not height balanced
            elif abs(left-right) > 1:
                return -1
            
            return 1 + max(left, right)
            
        return check(root) != -1