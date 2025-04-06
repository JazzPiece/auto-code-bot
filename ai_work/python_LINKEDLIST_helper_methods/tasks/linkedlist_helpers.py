from linkedlist import LinkedList

def create_linkedlist(arr):
    ll = LinkedList()
    for data in arr:
        ll.append(data)
    return ll

def reverse_linkedlist(ll):
    prev = None
    current = ll.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    ll.head = prev

def delete_node(ll, key):
    current = ll.head
    if current and current.data == key:
        ll.head = current.next
        current = None
        return
    prev = None
    while current and current.data != key:
        prev = current
        current = current.next
    if current is None:
        return
    prev.next = current.next
    current = None