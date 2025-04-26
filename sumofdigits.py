def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum = int(digit) + sum
    return sum
print(sum_of_digits(2789))