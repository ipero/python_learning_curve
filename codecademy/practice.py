# Write a function called digit_sum that takes a positive integer num as input
# and returns the sum of all that number's digits.
def digit_sum(num):
    digit_sum = 0
    number = str(num)
    for digit in number:
        digit_sum += int(digit)

    return digit_sum

print digit_sum(1234)

# find factorial of positive number
def factorial(n):
    factorial = 1
    if n == 0:
        return factorial
    for i in range(n, 0, -1):
        factorial *= i
    return factorial
print factorial(4)

# find if number is prime number (can be divided even by itself of 1)
# 2, 3, 5, 7 and 11 are prime numbers
