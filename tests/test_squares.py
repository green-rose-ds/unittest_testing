import unittest

class SmokeTest(unittest.TestCase):
    def test2_and2(self):
        self.assertEqual(2+2,4)

class TestSquare(unittest.TestCase):
    def test_root_of0(self):
        self.assertEqual(sq_num(0),0)

if __name__ == "main":
    unittest.main()