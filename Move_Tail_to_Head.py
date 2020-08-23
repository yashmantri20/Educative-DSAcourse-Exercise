
# Move Tail to Head

def move_tail_to_head(self):
    curr_node = self.head 
    while curr_node.next:
        prev = curr_node
        curr_node = curr_node.next
    prev.next = None
    curr_node.next = self.head
    self.head = curr_node
    return curr_node