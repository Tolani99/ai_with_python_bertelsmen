"""
Write a program which accepts a string from console 
and print the characters that have even indexes, then prime
indexes seperately
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_characters_by_index(string):
    even_indexes = ""
    odd_indexes = ""
    prime_indexes = ""

    for index, char in enumerate(string):
        if index % 2 == 0:
            even_indexes += char
        else:
            odd_indexes += char

        if is_prime(index):
            prime_indexes += char

    print("Characters at even indexes:", even_indexes)
    print("Characters at odd indexes:", odd_indexes)
    print("Characters at prime indexes:", prime_indexes)

# Accept input string from console
input_string = input("Enter a string: ")

# Print characters at even, odd, and prime indexes separately
print_characters_by_index(input_string)
