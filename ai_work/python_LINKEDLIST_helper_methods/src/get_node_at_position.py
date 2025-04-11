class LinkedList:
    def get_node_at_position(self, position):
        current_node = self.head
        for _ in range(position):
            if current_node is None:
                return None
            current_node = current_node.next
        return current_node

# Example usage:
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# node = ll.get_node_at_position(1)
# print(node.data)  # Output: 2