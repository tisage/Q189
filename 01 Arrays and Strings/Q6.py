# Q6. Compress String, aabcccccaaa -> a2b1c5a3
# assume only letters a-z
# if compressed string >= original string, return original


def StringCompress(string):
    if len(string) == 0:
        return string
    # Use compressedParts list
    compressedParts = []
    # counter for repeat character
    counter = 0

    for i in range(len(string)):
        # append string[] and string count into list
        if i != 0 and string[i] != string[i - 1]:
            compressedParts.append(string[i - 1] + str(counter))
            # finish this charcater compress and reset count
            counter = 0
        counter += 1
    # append the last string[] and its count
    compressedParts.append(string[-1] + str(counter))

    # combine compress parts list into a single string
    compressedString = ''.join(compressedParts)

    # compare with original
    if len(compressedString) < len(string):
        return compressedString
    else:
        return string

if __name__ == "__main__":
    import sys
    print(StringCompress(sys.argv[-1]))
