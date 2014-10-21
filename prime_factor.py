"""Prime Factorization - Have the user
enter a number and find all Prime Factors
(if there are any) and display them."""

#Check if the number is prime.
def is_prime(n):
	if n % 2 == 0:
		return False

	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

input = int(raw_input("Enter a number >> "))
factors = [1]
#Two is always prime, so treat it on the side.
if input % 2 == 0:
	factors.append(2)

#Check numbers from 3 and check if it's a interger.
for x in range(3, int(input / 2) + 1):
	if input % x == 0:
		if is_prime(x) == True:
	 			factors.append(x)

print factors
