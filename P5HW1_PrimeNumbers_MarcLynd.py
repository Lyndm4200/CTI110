# A brief description of the project
# Date
# CTI-110 P5HW1 - Prime Numbers
# Your Name
#
def main():
    # Ask user to input a number to see if it is a prime number or not
    num = int(input("Please enter a number"))
    return is_prime(num)
# Create function to determine if a number is prime
def is_prime(num):
    # If less or equal to 1, not prime
    if num <= 1:
        status = False
    # 2 is prime
    elif num == 2:
        status = True
    # Start at 3 and in increments of 2 multiply the square root of the
    # number by .5 and add 1, if it equals 0 it is not prime
    elif for x in range(3,num**(0.5)+1,2):
        if num % x == 0:
            status = False
        # Otherwise it is prime
        else:
            status = True
    # Closing else 
    else:
        status = True
    return status
main()
