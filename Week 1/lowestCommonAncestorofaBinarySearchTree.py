class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def lowestCommonAncestor(self, root, p, q):
        
        #While a node exist
        while root:
            #If the value of the node is bigger than the
            #value of the given two nodes discard the right side
            if root.val > p.val and root.val > q.val:
                root = root.left
             #If the value of the node is smaller than the
            #value of the given two nodes discard the left side
            elif  root.val < p.val and root.val < q.val:
                root = root.right
            #You found the lowest common ancestor
            else:
                return root
          
   