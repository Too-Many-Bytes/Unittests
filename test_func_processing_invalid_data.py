import unittest
from random import randint
from Unittests.functions import *


class TestOnInvalidData(unittest.TestCase):
    with open('cases_invalid.txt', 'w', encoding='utf-8') as f:
        for _ in range(10):
            for _ in range(8):
                element = ''
                for _ in range(randint(1, 8)):
                    element += chr(randint(58, 90))
                f.write(element + ' ')
            f.write('\n')

    def setUp(self) -> None:
        self.data = read_file('cases_invalid.txt')

    def test_min_on_invalid_str(self):
        for i in self.data:
            with self.subTest(i=i):
                self.assertEqual(find_min(i), 'Некорректный ввод!')

    def test_max_on_invalid_str(self):
        for i in self.data:
            with self.subTest(i=i):
                self.assertEqual(find_max(i), 'Некорректный ввод!')

    def test_sum_on_invalid_str(self):
        for i in self.data:
            with self.subTest(i=i):
                self.assertEqual(find_sum(i), 'Некорректный ввод!')

    def test_product_on_invalid_str(self):
        for i in self.data:
            with self.subTest(i=i):
                self.assertEqual(find_product(i), 'Некорректный ввод!')


if __name__ == '__main__':
    unittest.main()
