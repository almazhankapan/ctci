class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    
def check_subtree(t1, t2):
    order1 = pre_order(t1, "")
    order2 = pre_order(t2, "")
    
    # If the second preorder exists within the first
    return order2 in order1
    
def pre_order(root, order):
# If none, put in a X placeholder
    if root is None:
        return "X"

    # Get left and right trees
    left = pre_order(root.left, order)
    right = pre_order(root.right, order)
    # Return preorder traversal
    return str(root.data) + ' ' + left + ' ' + right