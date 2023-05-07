"""Function tekshirirsh"""
import math

# import unittest
# from tubSonmi import tubSonmi

# def get_full_name(ism, familiya, age=""):
#     if age:
#         return f"{ism} {familiya} {age}".title()
#     else:
#         return f"{ism} {familiya}".title()


# class tubSonTest(unittest.TestCase):
#     def test_true(self):
#         self.assertTrue(tubSonmi(7))
#         self.assertTrue(tubSonmi(193))
#         self.assertTrue(tubSonmi(547))

#     def test_false(self):
#         self.assertFalse(tubSonmi(6))
#         self.assertFalse(tubSonmi(265))
#         self.assertFalse(tubSonmi(489))


# unittest.main()

# exam problems


def get_num(a, b, c):
    return max(a, b, c)


#  2
def get_list1(my_list):
    words = [word.title() for word in my_list]
    return words


#   =>  3
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


#   =>  4
