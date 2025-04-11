def get_middle_element(list):
    slow = list.head
    fast = list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data