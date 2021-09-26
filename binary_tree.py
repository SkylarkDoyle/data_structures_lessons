#binary Tree
#Note----    O(1) + O(1) = O(1),          O(1) + O(n) = O(n),      O(1) + O(n^2) = O(n^2)

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

        
#Time Complexity -> O(1) + O(1) = O(1)   no recursion or loop -- Constant Time
def count_binaryAmount(root):
    if root is None:
        return 0   #T= O(1)
    else:
        return root.data + root.right.data + root.left.data  #T= O(1)


