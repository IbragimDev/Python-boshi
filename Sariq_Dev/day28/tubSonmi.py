# def tubSonmi(n):
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n < 2:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):  # faqat toq sonlarni tekshiramiz
#         if n % i == 0:
#             return False
#     return True


# import unittest
# from name import get_num, get_list1, get_even_numbers


# class TrueTest(unittest.TestCase):
#     def test_get_answer(self):
#         name = get_num(2, 5, 8)
#         self.assertEqual(name, 8)

#     def test_get_list1(self):
#         result = get_list1(["salom", "dunyo", "python", "sariq", "dark", "qizil"])
#         self.assertEqual(result, ["Salom", "Dunyo", "Python", "Sariq", "Dark", "Qizil"])

#     def test_get_even_numbers(self):
#         result = get_even_numbers(range(50))
#         self.assertListEqual(
#             result,
#             [
#                 0,
#                 2,
#                 4,
#                 6,
#                 8,
#                 10,
#                 12,
#                 14,
#                 16,
#                 18,
#                 20,
#                 22,
#                 24,
#                 26,
#                 28,
#                 30,
#                 32,
#                 34,
#                 36,
#                 38,
#                 40,
#                 42,
#                 44,
#                 46,
#                 48,
#             ],
#         )


# unittest.main()
