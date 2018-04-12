# Q9. check whether two strings are rotated of each other
# Given a method to check sub-string

def isSubstring(string, sub):
    return string.find(sub) != -1

def isRotation(st1, st2):
	if len(st1)==len(st2) != 0:
		return isSubstring(st1+st1, st2)
	return False

if __name__ == "__main__":
	import sys
	a = 'waterbottle'
	b = 'erbottlewat'
	print(isRotation(a,b))