# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.target = targetSum  #declaring the targetsum globally
        self.result = []  #list to store the path which adds upto targetsum
        self.recurr(root,0,[])  #calling and passing root, currsum,pathlist to store the path of the currsum
        
        return self.result  #returning the result
    
    
    def recurr(self,root,currsum,path):  #recurrsion function
        if root == None:  #if the root is none recurrsion starts to unfold
            return
        
        currsum+=root.val  #adding the currsum and root value 
        path.append(root.val)  #wea re appending the root value which we used to calculate currsum
        
        
        self.recurr(root.left,currsum,path)  #calling the recurrsion function for the left node of the root
        
        if root.left ==None and root.right==None:  #if the right node and left node of the root is null we are checking whether the targetsum is equals to currsum if it is equal we are doing shallow copy for the path
            if currsum == self.target:
                temp = path[:]
                self.result.append(temp)  #we are appending the copied path into the result array
                
                
        self.recurr(root.right,currsum,path)  #calling the recurrsion function for the left node of the root
        path.pop()  #we are popping out all the elements in the path list
        