# Q2.3 Delete Middle Node.

def removeMid(node):
	node.data = node.next.data
	node.next = node.next.next

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

if __name__ == '__main__':
    A = Node(1, Node(3, Node(5, Node(7))))
    temp = A
    while temp:
        print(temp.data)
        temp = temp.next
    print("")
    removeMid(A.next)
    temp = A
    while temp:
        print(temp.data)
        temp = temp.next