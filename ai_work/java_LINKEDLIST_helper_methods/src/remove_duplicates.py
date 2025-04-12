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