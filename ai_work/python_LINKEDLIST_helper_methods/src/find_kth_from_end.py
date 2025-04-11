class LinkedList:
    def find_kth_from_end(self, k):
        slow_ptr = self.head
        fast_ptr = self.head
        for _ in range(k):
            if fast_ptr is None:
                return None
            fast_ptr = fast_ptr.next
        while fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return slow_ptr

# Example usage:
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# node = ll.find_kth_from_end(2)
# print(node.data)  # Output: 2