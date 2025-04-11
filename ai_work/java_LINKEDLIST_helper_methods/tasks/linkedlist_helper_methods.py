from linkedlist_operations import LinkedList

def search(llist, key):
    current = llist.head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False

def size(llist):
    count = 0
    current = llist.head
    while current:
        count += 1
        current = current.next
    return count

def reverse(llist):
    prev = None
    current = llist.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    llist.head = prev

# Usage example:
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# reverse(llist)
# llist.display()  # Output: 3 2 1