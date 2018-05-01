# Q2.4 Partition a Linked list
# Use two nodes for each partition
# return joined final two linked lists

def partitionList(head, k):
    p1_head, p1_tail = None, None
    p2_head, p2_tail = None, None
    current = head
    # travese input linked list
    while current:
        # left partition
        if current.data < k:
            # check whether p1_head and p1_tail is empty
            # if not empty, assign current tail with current node
            # tail node point to current node and move tail cursor
            if p1_head:
                p1_tail.next = current
                p1_tail = current
            # if empty, initalize head and tail node
            else:
                p1_head = current
                p1_tail = current
        # right partition
        else:
            if p2_head:
                p2_tail.next = current
                p2_tail = current
            else:
                p2_head = current
                p2_tail = current
        current = current.next
    # set p2_tail = None, otherwise, loop list
    p2_tail.next = None
    p1_tail.next = p2_head
    return p1_head


class Node():

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

if __name__ == '__main__':
    A = Node(1, Node(3, Node(5, Node(7, Node(3, Node(2))))))
    temp = A
    while temp:
        print(temp.data)
        temp = temp.next
    print("")
    temp = partitionList(A, 5)
    while temp:
        print(temp.data)
        temp = temp.next
