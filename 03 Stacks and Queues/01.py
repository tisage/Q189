# Q3.1 Three in One. Use a single array to implement three stacks


class Stacks():

    def __init__(self, size):
    	self.numStacks = 3
    	self.array = [0] * (size * self.numStacks)
    	self.sizes = [0] * self.numStacks
    	self.stackSize = size

    def push(self, item, stackNum):


    def pop(self, stackNum):


if __name__ == '__main__':
    newstack = Stacks()
