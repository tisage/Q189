# Q2.8 Return node when there is any intersection of two singly linked lists.
# Intersection is defined based on reference, not value


def loopDetect(node):
    nodes = {}
    head = node
    while head:
        if head in nodes:
            return head
        nodes[head] = True
        head = head.next
    return None


class Node():

    def __init__(self, data, next=None):
        self.data, self.next = data, next


if __name__ == '__main__':
    node = Node(1)
    A = Node(7)
    C = Node(1, Node(3, Node(5, A)))
    D = Node(2, Node(4, Node(6, A)))
    A.next = D
    print(loopDetect(C).data)
    print(loopDetect(D).data)
