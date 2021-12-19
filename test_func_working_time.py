import unittest
from random import randint
from time import time
from functions import *


@unittest.expectedFailure
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


if __name__ == '__main__':
    unittest.main()
