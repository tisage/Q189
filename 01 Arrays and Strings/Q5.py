# Q5. Check two strings whether they are one edit or zero away
# three cases: replace, remove, insert


def OneAway(str1, str2):
    if len(str1) == len(str2):
        return OneEditReplace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return OneEditInsert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return OneEditInsert(str2, str1)
    else:
        return False

# search and check by each character
# editedCount > 1, return false

def OneEditReplace(str1, str2):
    edited = False
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True

# shirft case, searfh from two strings by character
# if edited, cursor index from longer string shift +1
# else move both cursor index
def OneEditInsert(str1, str2):
    edited = False
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


if __name__ == "__main__":
    import sys
    print(OneAway(sys.argv[-2], sys.argv[-1]))
