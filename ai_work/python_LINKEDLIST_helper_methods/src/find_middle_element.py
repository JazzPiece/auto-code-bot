class LinkedList:
    def find_middle_element(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr