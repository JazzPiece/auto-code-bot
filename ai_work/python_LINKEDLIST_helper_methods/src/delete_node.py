class LinkedList:
    def delete_node(self, key):
        current_node = self.head
        if current_node is not None:
            if current_node.data == key:
                self.head = current_node.next
                current_node = None
                return
        while current_node is not None:
            if current_node.data == key:
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node == None:
            return
        prev_node.next = current_node.next
        current_node = None