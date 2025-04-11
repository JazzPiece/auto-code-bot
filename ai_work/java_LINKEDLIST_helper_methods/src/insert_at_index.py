class LinkedList:
    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < index-1:
            current = current.next
            count += 1
        if not current:
            return
        new_node.next = current.next
        current.next = new_node