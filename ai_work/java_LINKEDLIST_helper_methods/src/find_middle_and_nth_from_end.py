def get_middle_element(list):
    slow = list.head
    fast = list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

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