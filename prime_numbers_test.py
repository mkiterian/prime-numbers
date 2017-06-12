import unittest
from prime_numbers import generate_prime_numbers

class PrimeNumberTest(unittest.TestCase):
	
	def test_generates_correct_prime_numbers(self):
		#tests if function returns correct values given n is an integer
		actual = generate_prime_numbers(10)
		expected = [2,3,5,7]
		self.assertEqual(actual, expected, msg='Expected [2,3,5,7] when n is 10')

	def test_n_is_an_integer(self):
		#tests if n is an integer 
		with self.assertRaises(TypeError, msg='n is not an integer'):
			generate_prime_numbers('number')

if __name__ == '__main__':
	unittest.main()

