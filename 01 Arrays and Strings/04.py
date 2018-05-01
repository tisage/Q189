# Q1.4, Check whether a string is a permutation of a palindrome.
# ignore space


def isPalindrome(string):
	# use dictionary Counter() to summerize frequency of each character
	counter=Counter()
	# lower case all character
	# remove spaces
	for letter in string.lower().replace(" ", ""):
		counter[letter]+=1

	# odd_count of each letters should <= 1
	# so that permutaiton of a palindrome exists
	odd_count = 0
	for count in counter.values():
		odd_count += count%2
		if odd_count > 1:
			return False
	return True

if __name__ == "__main__":
	import sys
	from collections import Counter
	print(isPalindrome(sys.argv[-1]))