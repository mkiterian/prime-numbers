def generate_prime_numbers(number):
	#create empty lists for prime numbers and numbers that have been tested
	primes = []
	tested = [1]

	try:
		#for every num from 1 to limit
		if number > 0:
			for num in range(1, number+1):

				#create a list to hold factors of the num
				factors = []

				#check if num is divisible by x in the tested list
				for i in range(len(tested)):
					#if num is divisible by x, add x to the factors list 
					if num % tested[i] == 0:
						factors.append(tested[i])

				#add num to it's factors list
				factors.append(num)
				set_factors = set(factors)
				tested.append(num)

				if len(set_factors) == 2:
					primes.append(num)

			return primes
		else:
			return 'N should be a positive integer'
	except TypeError:
		raise TypeError
            
print(generate_prime_numbers(100000))
