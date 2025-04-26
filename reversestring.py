def reverse_string(string):
    reversed_string = "" # starts with an empty string
    for char in string: # use of loop to go through characters
        reversed_string = char + reversed_string # order should be character then the reversed string
    return reversed_string
print(reverse_string("hate")) # output should be reversed