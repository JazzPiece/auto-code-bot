def merge_linkedlists(list1, list2):
    current = list1.head
    while current.next:
        current = current.next
    current.next = list2.head