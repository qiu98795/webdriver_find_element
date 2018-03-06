from calculator import *
from StarEnd import *

class Test_add(Setup_tearDown):
    def test_add1(self):
        j=Math(10,8)
        self.assertEqual(j.add(),18)

    def test_add2(self):
        j=Math(10,10)
        self.assertEqual(j.add(),20)