"""
To solve a quadratic equation
"""

def solve_quadratic(a, b, c):

	# return the quadratic formulae
	return ((-b + (b**2 - 4*a*c)**(1/2))/(2*a), (-b-(b**2 - 4*a*c)**(1/2))/(2*a))

#print(solve_quadratic(1, -5, 6))

# input required parameters
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# print the solution to the quadratic equation
print(solve_quadratic(a, b, c))
