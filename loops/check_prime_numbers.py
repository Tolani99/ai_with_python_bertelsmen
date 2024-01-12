check_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]

for num in check_prime:
    # Check if the number is 2
    if num == 2:
        print("{} IS a prime number".format(num))
        continue

    # Search for factors, iterating through numbers ranging from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        # Number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number because {} is a factor of {}".format(num, i, num))
            break
    else:
        # If the loop completes without a break, the number is prime
        print("{} IS a prime number".format(num))

