'''
# printing first word
sentence = "Python is fun"
words = sentence.split()
print(words[1])

# reverse a word
sentence = "python is fun"
print(sentence[:: -1])

#another way for reversing word
text = "Cat"
backwards = "".join(reversed(text))
print(backwards)

# for first and last character and output in different line
word = "Laptop"
print(word[0])
print(word[-1])

# second character
word = "Laptop"
print(word[1])

# second to last character
word = "Laptop"
print(word[4])
'''

# first three character
words = "keyboard"
print(words[:3])

# last three characters
words = "Keyboard"
print(words[-3:])

# without its first character
words = "Keyboard"
print(words[1:])

# without last character
words = "Keyboard"
print(words[:-1])