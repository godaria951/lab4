import unittest

class ObjectReuseTests(unittest.TestCase):
    def test_primitive_interning(self):
    
        a = 4123
        b = 4123
        self.assertIs(a, b, "Small integers should have the same id (interned)")

        x = "ghj"
        y = "ghj"
        self.assertIs(x, y, "Short strings should have the same id (interned)")

    def test_heap_allocation(self):
        
        list1 = []
        list2 = []
        self.assertIsNot(list1, list2, "Different lists should have different ids")

        dict1 = {}
        dict2 = {}
        self.assertIsNot(dict1, dict2, "Different dicts should have different ids")

        class CustomClass:
            pass

        obj1 = CustomClass()
        obj2 = CustomClass()
        self.assertIsNot(obj1, obj2, "Different instances of a class should have different ids")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ObjectReuseTests)
    unittest.TextTestRunner().run(suite)
