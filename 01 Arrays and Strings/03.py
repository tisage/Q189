# URLify to replace all spaces in a string with %20 and ignore tail space

def URLify(string):
	# The method rstrip() returns a copy of the string in which 
	# all chars have been stripped from the end of the string 
	# (default whitespace characters)
	return string.strip().replace(" ", "%20")

if __name__ =="__main__":
	import sys
	print(URLify(sys.argv[-1]))
