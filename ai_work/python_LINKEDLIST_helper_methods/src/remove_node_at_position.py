class LinkedList:
    def remove_node_at_position(self, position):
        if position == 0:
            self.head = self.head.next
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None or current_node.next is None:
                return
            current_node = current_node.next
        if current_node.next is not None:
            current_node.next = current_node.next.next