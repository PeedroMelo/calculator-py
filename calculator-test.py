import unittest
from functions import calculate

class SimpleTest(unittest.TestCase):
  
  def test(self):         
    self.assertEquals(4, calculate(2, 2))

if __name__ == '__main__': 
    unittest.main()