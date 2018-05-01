# Q2-1. Remove duplicates from an unsorted linked list.


def removeDuplicate(head):
    # traverse the linked-list using a temp node
	node = head
	if node:
        # use a dictionary to record value
		values= {node.data: True}
		while node.next:
            # if value exists, link this node to the next node
            # move to the next of next node
			if node.next.data in values:
				node.next = node.next.next
			else:
            # if value not exists in the dic, save this value in dic
            # move to the next node
				values[node.next.data] = True
				node = node.next
	return head

# Not using library, create a Node class
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

if __name__ == '__main__':
    A = Node(1, Node(3, Node(3, Node(5, None))))
    temp = A
    while temp:
        print(temp.data)
        temp = temp.next
    print("")
    removeDuplicate(A)
    temp = A
    while temp:
        print(temp.data)
        temp = temp.next
