import unittest

def calculate(a, b):
  return a * b

class SimpleTest(unittest.TestCase):
  
  def test(self):         
    self.assertEquals(4, calculate(2, 2))

if __name__ == '__main__': 
    unittest.main()