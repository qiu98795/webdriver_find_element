from calculator import *
from StarEnd import *

class Test_sub(Setup_tearDown):
    def test_sub1(self):
        i=Math(5, 3)
        self.assertEqual(i.sub(),2)

    def test_sub2(self):
        i=Math(10, 2)
        self.assertEqual(i.sub(),8)
