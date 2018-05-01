# Q2.2 Return kth element from the last of a singly linked list.

# use two pointer that k elements aparts and traverse the list
def kList(head, k):
    p1, p2 = head, head
    for i in range(k):
        if not p1:
            return None
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2

# Not using library, create a Node class
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

if __name__ == '__main__':
    A = Node(1, Node(3, Node(5, Node(7, None))))
    temp = A
    while temp:
        print(temp.data)
        temp = temp.next
    print("")
    print(kList(A, 2).data)

	