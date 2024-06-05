import unittest


class Calculator:

  def add(self, x1, x2):
    return x1 + x2

  def multiply(self, x1, x2):
    return x1 * x2

  def subtract(self, x1, x2):
    return x1 - x2

  def divide(self, x1, x2):
    if x2 != 0:
      return x1/x2


class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator()
    
  def test_add(self):
    self.assertEqual(self.calculator.add(4,7), 11)
    
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)
    self.assertEqual(self.calculator.subtract(5,10), -5)
    
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)
    self.assertEqual(self.calculator.multiply(2,0), 0)
    
  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,2), 5)
    self.assertEqual(self.calculator.divide(0,2), 0)
    
    
if __name__ == "__main__":
  unittest.main()
