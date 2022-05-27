import unittest
from translator import french_to_english, english_to_french

class Test_e2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(" "), " ")
    
    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class Test_f2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(" "), " ")
    
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()