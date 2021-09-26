#Note----    O(1) + O(1) = O(1),          O(1) + O(n) = O(n),      O(1) + O(n^2) = O(n^2)

class Node:
    def __init__(self, data):
        self.head = data
        self.next = None


#Time Complexity -> O(1) + O(1) + n * O(1)| bcs of the while loop | + O(1) + O(1)= O(n) 

def count_nodes(head):
    count = 1 #T= O(1)
    current_node = head  #T= O(1)

    while current_node.next is not None:
        current_node = current_node.next  #T= O(1)
        count += 1 #T= O(1)
    return count #T= O(1)
    
            
            
            
