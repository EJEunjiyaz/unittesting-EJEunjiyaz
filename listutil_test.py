import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
    
    def test_empty_list(self):
        self.assertListEqual( [], unique([]) )
    
    def test_single_item_many_time(self):
        self.assertListEqual( [5], unique([5,5,5,5,5,5]) )
    
    def test_two_items_many_time(self):
        self.assertListEqual( ['a', 'z'], unique(['a', 'z', 'z' ,'z', 'a', 'z']) )
    
    def test_single_item_string(self):
        self.assertListEqual( ['a'], unique('a') )
    
    def test_single_item_many_time_string(self):
        with self.assertRaises(TypeError):
            unique('a', 'a', 'a')
    
    def test_single_item_int(self):
        with self.assertRaises(TypeError):
            unique(123)
    
    def test_single_item_float(self):
        with self.assertRaises(TypeError):
            unique(90.09)
    
    def test_empty(self):
        with self.assertRaises(TypeError):
            unique()
    
    def test_two_list(self):
        with self.assertRaises(TypeError):
            unique( [1,2,3], [1,2,3] )


if __name__ == '__main__':
    unittest.main()