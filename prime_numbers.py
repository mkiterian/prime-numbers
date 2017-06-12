#tests if passed-in number is a prime number
def is_prime(num):
	if num < 2:
		return False

	for i in range(2, num):
		if num % i == 0:
			return False
	return True

#takes in a number and returns a list of prime numbers for zero to the number
def generate_prime_numbers(number):
	primes = []
	try:
		isinstance(number, int)
		if number > 0:			
			for num in range(2, number+1):
				if is_prime(num):
					primes.append(num)

			return primes
		else:
			return 'number should be a positive integer greater than 0'
	except TypeError:
		raise TypeError
