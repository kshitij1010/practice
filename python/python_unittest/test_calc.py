from unittest import TestCase, main
from unittest.case import expectedFailure

import calc


class TestCalc(TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5, 4), 9, "Ans should be 9")

    @expectedFailure
    def test_add2(self):
        self.assertEqual(calc.add(5, 5), 9, "Ans should be 9")

    def test_negative_div(self):
        self.assertRaises(ValueError, calc.div, 10, 0)

        with self.assertRaises(ValueError):
            calc.div(15, 0)

if __name__ == '__main__':
    main(verbosity=3)
