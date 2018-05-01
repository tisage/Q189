#Q2.6 Check linked list is a palindrome

def isPalindrome(node):
	forward = node
	backward = reverse(node)
	while forward:
		if forward.data != backward.data:
			return False
		forward = forward.next
		backward = backward.next
	return True

# not using stack 
# but use a temp node to copy the rest of input node
# reversely link node
def reverse(node):
	prev = None
	temp = copy(node)
	while temp:
		next = temp.next
		temp.next = prev
		prev = temp
		temp = copy(next)
	return prev

def copy(node):
	if node:
		return Node(node.data, node.next)
	else:
		return None

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
    A = Node(1, Node(2, Node(3)))
    printList(A)
    print("")
    print(isPalindrome(A))
    B = Node(1, Node(2, Node(1)))
    printList(B)
    print("")
    print(isPalindrome(B))
