# prime-numbers
This repo contains a generate_prime_numbers() that takes in argument n
and generates prime numbers from 0 upto the number

Usage:
1. git clone https://github.com/mkiterian/prime-numbers.git
3. ensure the latest python 3 is installed
2. dependencies can be found in requirements.txt
3. tests for the function are included in prime_numbers_test.py
4. call generate_prime_numbers() and pass a positive number(n)
5. the returned value should be the list of prime numbers from 0 to n

How it works:
- The function generate_prime_numbers takes in an argument 'number'
- it creates a variable to hold the list of prime numbers initiated as an empty list
- it checks to see if the number is an integer, if not a type error is raised
- if the number is a positive integer then(else message is displayed asking for right argument value)
- if its within the 2 to the number+1, the *is_prime function is called
- if is_prime returns true the number is added to the primes list
- the primes list is returned

* the is_prime function tests if a number is prime by
- first checking if its less than 2(as 2 is the smallest prime number)returns false in this case
- if the modulus of the number and any number between 2 and itself it return false
- otherwise the number is_prime returns true 


* the time complexity of this function is linearly related to size of the input;
  a large number will take longer to compute