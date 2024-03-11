"""
Write a program that computes the value of 
x+xx+xxx+xxxx with a given digit as the value of x
if the input is 9 then, the output should be 11106
"""
def compute_expression_value(x):
    # Convert the input digit to a string
    x_str = str(x)
    
    # Compute each term of the expression and sum them up
    result = int(x_str) + int(x_str*2) + int(x_str*3) + int(x_str*4)
    
    return result

# Example usage:
input_digit = 9
output = compute_expression_value(input_digit)
print(output)
