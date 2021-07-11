class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        out=[]
        def inorder(root):
            if root!=None:
                inorder(root.left)
                out.append(root.val)
                inorder(root.right)
            return out
        return inorder(root)

#note: you can have nested functions