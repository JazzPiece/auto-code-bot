def remove_duplicates(self):
    current = self.head
    seen = set()
    prev = None
    while current:
        if current.data in seen:
            prev.next = current.next
            current = None
        else:
            seen.add(current.data)
            prev = current
        current = prev.next

class LinkedList:
    def reverse_linkedlist(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev