import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    # part 1
    # because we are in a class must pass the self keyword
    # def test_function_return_True(self):
    # self.assertTrue(even_number_of_evens([]))

    def test_throws_error_if_value_passed_in_it_is_not_list(self):
        # it checks to see if a TypeError is raised  when the function is called with the value 4
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()
