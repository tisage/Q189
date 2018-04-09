# check whether two strings are permutation of the other

# sumit and mtisu are permutation of each other? True
# Check counter frequency of each string

def isPermut(str1, str2):
	if len(str1) != len(str2):
		return False
	counter = Counter()
	for letter in str1:
		counter[letter] += 1
	# print(counter)
	for letter in str2:
		if counter[letter]==0:
			return False
		counter[letter] -= 1
	return True


if __name__ == "__main__":
	import sys
	from collections import Counter
	print(isPermut(sys.argv[-2], sys.argv[-1]))
    