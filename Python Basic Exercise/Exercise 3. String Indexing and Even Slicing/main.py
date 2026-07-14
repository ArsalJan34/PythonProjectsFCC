word = "python"
print("Original string is : ",word)
# we are using list slicing here
# format : [start:stop:state]
even_Char = word[0::2]
print("printing only even index characters: ")
for char in even_Char:
  print(char)

# printing only odd index characters

word2 = "python"
print("the original word is ",word2)

odd_Char = word2[1::2]

print("printing only odd index characters : ")
for char2 in odd_Char:
  print(char2)
