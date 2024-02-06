n = int(input("Enter any number: "))
result = 1
for i in range(n+1):
	if i != 0:
		result *= i
print("The factorial of {} is {}".format(n, result))	
