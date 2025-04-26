def sum_list(numbers): #defining a function called sum_list with parameter
    total = 0 #initializing total to zero
    for number in numbers:# for loop to add numbers
        total = total + number
    return total

print(sum_list([15,70,15]))