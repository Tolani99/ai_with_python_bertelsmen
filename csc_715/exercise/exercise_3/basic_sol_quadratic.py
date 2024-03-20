"""
To solve a quadratic equation
"""

def solve_quadratic(a, b, c):
	return ((-b + (b**2 - 4*a*c)**(1/2))/(2*a), (-b-(b**2 - 4*a*c)**(1/2))/(2*a))

print(solve_quadratic(1, -5, 6))
