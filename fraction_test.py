import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(2), Fraction(1,1)+Fraction(1,1))
        self.assertEqual(Fraction(-5,2), Fraction(-1,2)+Fraction(-4,2))
        self.assertEqual(Fraction(5,28), Fraction(3,7)+Fraction(-1,4))

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
        f = Fraction(-1,0)
        g = Fraction(-3,0)
        h = Fraction(2,0)
        self.assertTrue(f == g)
        self.assertFalse(f == h)
        self.assertFalse(g == h)
        
    def test_mul(self):
        self.assertEqual(Fraction(1,2), Fraction(2,3)*Fraction(3,4))
        self.assertEqual(Fraction(1), Fraction(-1,2)*Fraction(-4,2))
        self.assertEqual(Fraction(-3,28), Fraction(3,7)*Fraction(-1,4))
    
    def test_sub(self):
        self.assertEqual(Fraction(0), Fraction(1)-Fraction(1))
        self.assertEqual(Fraction(3,2), Fraction(-1,2)-Fraction(-4,2))
        self.assertEqual(Fraction(19,28), Fraction(3,7)-Fraction(-1,4))
    
    def test_neg(self):
        self.assertEqual(Fraction(1), Fraction.__neg__(-1))
        self.assertEqual(Fraction(0), Fraction.__neg__(-0))
        self.assertEqual(Fraction(50,0), Fraction(-20,0).__neg__())
    
    def test_input_str(self):
        with self.assertRaises(ValueError):
            Fraction("a")
            Fraction("b",2)
    
    def test_input_many(self):
        with self.assertRaises(TypeError):
            Fraction(1,1,1,1)
            Fraction("a","b",1,5.1,3,3,3,3)
        
            

if __name__ == '__main__':
    unittest.main()