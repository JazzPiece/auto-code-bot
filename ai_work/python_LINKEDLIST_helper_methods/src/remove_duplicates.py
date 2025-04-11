class LinkedList:
    def remove_duplicates(self):
        current = self.head
        seen_values = set()
        prev = None
        while current:
            if current.data in seen_values:
                prev.next = current.next
            else:
                seen_values.add(current.data)
                prev = current
            current = current.next