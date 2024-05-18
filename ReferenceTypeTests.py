import unittest

class ReferenceTypeTests(unittest.TestCase):
    def test_array_passed_by_reference(self):
        value = [1, 2, 3]
        self.increment_each(value)
        self.assertEqual(value, [2, 3, 4])

    @staticmethod
    def increment_each(array):
        for i in range(len(array)):
            array[i] += 1

    def test_custom_class_passed_by_reference(self):
        custom_class = self.CustomClass(10)
        self.increment(custom_class)
        self.assertEqual(custom_class.value, 11)

    @staticmethod
    def increment(custom_class):
        custom_class.value += 1

    class CustomClass:
        def __init__(self, value):
            self.value = value

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ReferenceTypeTests)
    unittest.TextTestRunner().run(suite)
