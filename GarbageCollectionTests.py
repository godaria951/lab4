import gc
import unittest

class TestGarbageCollector(unittest.TestCase):
    def test_garbage_collector(self):
        
        obj = type('TestObject', (object,), {})()
        obj_id = id(obj)

        del obj

        gc.collect()

        for obj in gc.get_objects():
            if id(obj) == obj_id:
                self.fail('Об’єкт не був знищений')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGarbageCollector)
    unittest.TextTestRunner().run(suite)
