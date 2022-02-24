import unittest
import random
import sys
sys.path.append('../src')
from src.calculator import ConversionRate

class TestCalc(unittest.TestCase):
    def test_int(self): 

        Number1 = random.randint(0,1000000)
        Number2 = random.randint(0,1000000)

        ExpectedValue = Number1 + Number2

        result = ConversionRate(Number1, Number2)

        self.assertEqual(result, ExpectedValue)
    
    def test_float(self): 

        Number1 = random.random()
        Number2 = random.random()

        ExpectedValue = Number1 + Number2

        result = ConversionRate(Number1, Number2)

        self.assertEqual(result, ExpectedValue)

    def test_uniform(self): 

        Number1 = random.uniform(0,1000000)
        Number2 = random.uniform(0,1000000)

        ExpectedValue = Number1 + Number2

        result = ConversionRate(Number1, Number2)

        self.assertEqual(result, ExpectedValue)


    