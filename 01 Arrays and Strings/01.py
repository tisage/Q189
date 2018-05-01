# check whether a string has all unique characters

def uniqueCharacter(string):
	letters = {}
	for letter in string:
		if letter in letters:
			return False
		print(letter)
		print(letters)
		# letters dictionary holds hash-value
		letters[letter] = 1
	return True

if __name__ == "__main__":
	import sys
	# use command line arguments, import sys
	print(uniqueCharacter(sys.argv[-1]))
    
