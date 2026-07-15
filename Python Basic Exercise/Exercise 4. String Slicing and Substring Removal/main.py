#  function to remove characters from a string starting from index 0 up to n and return a new string.
def remove_chars(word, n):
    print('Original string:', word)
    # extracting string from index n to the end
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

def remove_char(word,n):
    print("original string : ",word)

    rend = word[:n]
    return rend

print(remove_char("pyantive",2))
