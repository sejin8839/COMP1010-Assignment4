# Assignment written by: ___Sejin Yoon_______
def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


# The function takes a single parameter, number, which is the number whose digits we want to count.
#
# We initialize a variable count to zero, which will keep track of the number of digits in the given number.
#
# We use a while loop to keep dividing the number by 10 until the quotient becomes zero. In each iteration of the loop, we increment the count variable by 1.
#
# Finally, we return the count variable, which contains the number of digits in the given number.