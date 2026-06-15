import unittest
from ex2 import HighlandsPOS, InvalidQuantityError


class TestHighlandsPOS(unittest.TestCase):

    def test1(self):
        p = HighlandsPOS()

        p.add_to_order("P1", 2)
        p.add_to_order("F1", 1)

        r = p.calculate_total()

        self.assertEqual(r, 125000)

    def test2(self):
        p = HighlandsPOS()

        try:
            p.add_to_order("P1", -1)
            self.fail("must fail")
        except InvalidQuantityError:
            pass


if __name__ == "__main__":
    unittest.main()