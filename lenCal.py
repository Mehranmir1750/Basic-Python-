# Program to calculate length of string without using len()

def string_length(s):
    count = 0
    for char in s:   # loop through each character
        count += 1
    return count

# Example
text = "Hello"
print("String:", text)
print("Length of string:", string_length(text))
