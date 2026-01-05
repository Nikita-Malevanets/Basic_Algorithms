class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def insert_sorted(head, node):
    if not head or node.data < head.data:
        node.next = head
        return node

    cur = head
    while cur.next and cur.next.data < node.data:
        cur = cur.next

    node.next = cur.next
    cur.next = node
    return head


def sort_list(head):
    sorted_head = None
    cur = head

    while cur:
        nxt = cur.next
        sorted_head = insert_sorted(sorted_head, cur)
        cur = nxt

    return sorted_head


def merge_lists(a, b):
    result = None

    while a:
        nxt = a.next
        result = insert_sorted(result, a)
        a = nxt

    while b:
        nxt = b.next
        result = insert_sorted(result, b)
        b = nxt

    return result
