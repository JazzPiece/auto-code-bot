class LinkedList:
    def merge_sorted_lists(self, l2):
        dummy = Node()
        current = dummy
        p1, p2 = self.head, l2.head
        while p1 and p2:
            if p1.data < p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        current.next = p1 or p2
        self.head = dummy.next

# Example usage:
# ll1 = LinkedList()
# ll1.append(1)
# ll1.append(3)
# ll1.append(5)
# ll2 = LinkedList()
# ll2.append(2)
# ll2.append(4)
# ll2.append(6)
# ll1.merge_sorted_lists(ll2)
# ll1.print_list()  # Output: 1 2 3 4 5 6