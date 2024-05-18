import unittest

class ValueTypeTests(unittest.TestCase):
    def test_integer_passed_by_value(self):
        value = 10
        self.increment(value)
        self.assertEqual(value, 10)

    @staticmethod
    def increment(v):
        v += 1

    def test_custom_struct_passed_by_value(self):
        custom_struct = self.CustomStruct(10)
        self.increment_struct(custom_struct)
        self.assertEqual(custom_struct.value, 10)

    @staticmethod
    def increment_struct(custom_struct):
        custom_struct = ValueTypeTests.CustomStruct(custom_struct.value + 1)

    class CustomStruct:
        def __init__(self, value):
            self.value = value

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ValueTypeTests)
    unittest.TextTestRunner().run(suite)
