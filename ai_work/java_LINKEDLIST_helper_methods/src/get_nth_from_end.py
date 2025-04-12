def get_nth_from_end(self, n):
    slow = self.head
    fast = self.head
    count = 0
    while count < n:
        if not fast:
            return None
        fast = fast.next
        count += 1
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.data