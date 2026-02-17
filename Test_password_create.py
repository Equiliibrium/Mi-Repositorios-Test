import unittest
from main import generar_password

class TestPassword(unittest.TestCase):
    def test_largo_password(self):
        self.assertEqual(len(generar_password(20)), 20)
        
    def test_es_string(self):
        self.assertIsInstance(generar_password(10), str)
        
    def test_no_aletoriedad(self):
        pass1= generar_password(16)
        pass2= generar_password(16)
        self.assertNotEqual (pass1, pass2)
        
if __name__ == "__main__":
    unittest.main()
    
        
