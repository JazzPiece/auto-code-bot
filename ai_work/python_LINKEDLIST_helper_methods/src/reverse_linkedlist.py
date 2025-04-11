class LinkedList:
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage:
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.print_list()  # Output: 1 2 3
# ll.reverse_list()
# ll.print_list()  # Output: 3 2 1