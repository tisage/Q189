# Q2.5 Sum up two numbers represented by a linked List
# each node contains in reverse order digit


def sumList(node1, node2):
    # p1, p2 traverse two lists
    # carry to store carry number
    # result is a temp node to do sum up
    p1 = node1
    p2 = node2
    carry = 0
    result_head, result = None, None
    while p1 or p2 or carry:
        value = carry
        if p1:
            value += p1.data
            p1 = p1.next
        if p2:
            value += p2.data
            p2 = p2.next
        if result:
            result.next = Node(value % 10)
            result = result.next
        else:
            result = Node(value % 10)
            result_head = result
        # use floor divide
        carry = value // 10
    return result_head


class Node():

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def printList(node):
    temp = node
    while temp:
        print(temp.data)
        temp = temp.next

if __name__ == '__main__':
    A = Node(7, Node(1, Node(6)))
    printList(A)
    print("")
    B = Node(5, Node(9, Node(2)))
    printList(B)
    print("")
    printList(sumList(A, B))
