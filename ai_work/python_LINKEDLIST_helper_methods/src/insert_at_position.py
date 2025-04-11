class LinkedList:
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                return
            current_node = current_node.next
        if current_node is None:
            return
        new_node.next = current_node.next
        current_node.next = new_node