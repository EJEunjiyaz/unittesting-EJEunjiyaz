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
 
if __name__ == '__main__':
    unittest.main()