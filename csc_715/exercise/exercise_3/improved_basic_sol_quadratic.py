"""
To solve a quadratic equation
"""

def solve_quadratic(a, b, c):
	return ((-b + (b**2 - 4*a*c)**(1/2))/(2*a), (-b-(b**2 - 4*a*c)**(1/2))/(2*a))

a, b, c = map(int, input("Enter the value for a, b and c: ").split())

print(solve_quadratic(a, b, c))
