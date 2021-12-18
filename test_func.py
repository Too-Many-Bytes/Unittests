import unittest
from functools import reduce
from random import randint
from time import time
from functions import *


class TestCalculatingFunc(unittest.TestCase):
    with open('cases_results.txt', 'w', encoding='utf-8') as f:
        for _ in range(10):
            for _ in range(8):
                f.write(str(randint(-100, 100)) + ' ')
            f.write('\n')

    def setUp(self) -> None:
        self.data = read_file('cases_results.txt')

    def test_min(self):
        for i in self.data:
            self.assertEqual(find_min(i), min(i), 'Неверно найден минимум')

    def test_max(self):
        for i in self.data:
            self.assertEqual(find_max(i), max(i), 'Неверно найден максимум')

    def test_sum(self):
        for i in self.data:
            self.assertEqual(find_sum(i), sum(i), 'Неверно найдена сумма')

    def test_product(self):
        for i in self.data:
            self.assertEqual(find_product(i), reduce(lambda x, y: x * y, i), 'Неверно найдено произведение')

    def tearDown(self) -> None:
        pass


class TestWorkingTime(unittest.TestCase):
    with open('cases_time.txt', 'w', encoding='utf-8') as f:
        for i in range(1, 13002, 1000):
            for _ in range(100):
                f.write(str(randint(-10 ** i, 10 ** i)) + ' ')
            f.write('\n')

    def setUp(self) -> None:
        self.data = read_file('cases_time.txt')

    def test_working_time(self):
        i = 1
        for mass in self.data:
            with self.subTest(i=f'(-10 ** {i}; 10 ** {i}'):
                init_time = time()
                find_sum(mass)
                find_max(mass)
                find_min(mass)
                find_product(mass)
                final_time = time()
                self.assertLessEqual(final_time - init_time, 2, 'Превышено допустимое время работы программы: 2 сек.')
            i += 1000


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
            self.assertRaises(TypeError, find_min(i))

    def test_max_on_invalid_str(self):
        for i in self.data:
            self.assertRaises(TypeError, find_max(i))

    def test_sum_on_invalid_str(self):
        for i in self.data:
            self.assertRaises(TypeError, find_sum(i))

    def test_product_on_invalid_str(self):
        for i in self.data:
            self.assertRaises(TypeError, find_product(i))


if __name__ == '__main__':
    unittest.main()
    print(123)
