import unittest
from prime_numbers import generate_prime_numbers

class PrimeNumberTest(unittest.TestCase):	

	def test_n_is_an_integer(self):
		#tests if n is an integer 
		with self.assertRaises(TypeError, msg='n is not an integer'):
			generate_prime_numbers('number')

	def test_if_number_is_a_positive_integer(self):
		#test if number is a positive integer
		self.assertEqual(generate_prime_numbers(-10), 'N should be a positive integer', msg='Number Should be a positive integer')

	def test_if_returned_value_is_a_list(self):
		#check if number return is a list
		self.assertIsInstance(generate_prime_numbers(10), list)

	def test_if_number_of_returned_numbers_is_correct(self):
		#test if list returned has correct number 
		actual = len(generate_prime_numbers(11))
		expected = 5
		self.assertEqual(actual, expected, msg='Number of returned items is not as expected')

	def test_generates_correct_prime_numbers(self):
		#tests if function returns correct values given n is an integer
		actual = generate_prime_numbers(10)
		expected = [2,3,5,7]
		self.assertEqual(actual, expected, msg='Expected [2,3,5,7] when n is 10')

	
if __name__ == '__main__':
	unittest.main()

