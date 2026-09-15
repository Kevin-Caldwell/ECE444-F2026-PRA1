import unittest
from utils import Utils

class TestReverse(unittest.TestCase):
  def test_int(self):
    self.assertEqual(Utils.reversed(1001), 1001)
    self.assertEqual(Utils.reversed(1201), 1021)
    self.assertEqual(Utils.reversed(9), 9)
    self.assertEqual(Utils.reversed(1383848), 8483831)

  def test_str(self):
    with self.assertRaises(TypeError):
      Utils.reversed("")
      Utils.reversed("I")
      Utils.reversed("RACECAR")
      Utils.reversed("The quick brown fox")

  def test_float(self):
    with self.assertRaises(TypeError):
      Utils.reversed(0.0)
    with self.assertRaises(TypeError):
      Utils.reversed(19.3)
    with self.assertRaises(TypeError):
      Utils.reversed(10.3)
    with self.assertRaises(TypeError):
      Utils.reversed(100000000.0)
    with self.assertRaises(TypeError):
      Utils.reversed(1093.39948)

class TestFormatter(unittest.TestCase):
  def test_int(self):
    self.assertEqual(Utils.formatter(10), (1010, 12))
    self.assertEqual(Utils.formatter(39493), (1001101001000101, 115105))
  
  def test_str(self):
    with self.assertRaises(TypeError):
      Utils.formatter("")
    with self.assertRaises(TypeError):
      Utils.formatter("I")
    with self.assertRaises(TypeError):
      Utils.formatter("FIEJIFEJ")

  def test_float(self):
    with self.assertRaises(TypeError):
      Utils.formatter(10.9)
    with self.assertRaises(TypeError):
      Utils.formatter(0.0)
    with self.assertRaises(TypeError):
      Utils.formatter(1023939.13993)

if __name__ == "__main__":
  unittest.main()