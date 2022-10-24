# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        self.result = 0  #creating avariable to store the final result
        
        self.inordertraversal(root,0)  #calling and passing the root and result value in recurrsion
        
        return self.result  #returning the final result
    
    
    def inordertraversal(self,root,currsum):  #recurrsion function
        if root == None:  #if the root is none recursion starts to unfold
            return
        
        self.inordertraversal(root.left,currsum*10+root.val) #calling the recurrsion function for the left node and passing the present currsum
        
        if root.left == None and root.right == None:  #if both the leaf nodes are None we are adding it to the result
            self.result+=currsum*10 +root.val
        
        self.inordertraversal(root.right,currsum*10+root.val)  #calling the recurrsion function for the right node and passing the present currsum
        
        
        
        
        
        
        
        