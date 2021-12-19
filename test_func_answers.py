import unittest
from functools import reduce
from random import randint
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


if __name__ == '__main__':
    unittest.main()
