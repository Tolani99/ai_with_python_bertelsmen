def sort_words(input_str):
    # Split the input string into a list of words
    words = [word.strip() for word in input_str.split(',')]

    # Sort the list of words alphabetically
    sorted_words = sorted(words)

    # Join the sorted words into a comma-separated string
    sorted_str = ', '.join(sorted_words)

    return sorted_str

# Input from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Call the function to sort and print the words
sorted_sequence = sort_words(input_sequence)
print("Sorted sequence:", sorted_sequence)

