# Q2.7 Return node when there is any intersection of two singly linked lists.
# Intersection is defined based on reference, not value


def itersect(node1, node2):
    nodes = {}
    node = node1
    while node:
        nodes[node] = True
        node = node.next
    node = node2
    while node:
        if node in nodes:
            return node
        node = node.next
    return None


class Node():

    def __init__(self, data, next=None):
        self.data, self.next = data, next


if __name__ == '__main__':
    A = Node(1, Node(2, Node(3)))
    B = Node(1, Node(2, Node(3)))
    print(itersect(A, B))
    print("")
    node = Node(1)
    C = Node(1, Node(3, node))
    D = Node(2, Node(4, node))
    print(itersect(C, D))
