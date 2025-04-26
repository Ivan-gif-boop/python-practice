def number_checker(number):
    if number % 2 == 0: #Checking remainder through modulus
        return "Even number"
    else:
        return "Odd number" #if rem is not 0, odd no detected
print(number_checker(9768))