import unittest
from utils import Utils

class TestReverse(unittest.TestCase):
  def test_int(self):
    self.assertEqual(Utils.reversed(1001), 1001)
    self.assertEqual(Utils.reversed(1201), 1021)
    self.assertEqual(Utils.reversed(9), 9)


if __name__ == "__main__":
  unittest.main()