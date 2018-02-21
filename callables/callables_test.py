from unittest import main 
from unittest import TestCase

x = 10

class CallableClass(object):

    def __init(self):
        self.count = 0

    def __call__(self):
        return 'Called ' + (++self.count) + ' times'

class UnCallableClass(object):

    def __init__(self):
        self.count = 0

class CallableTestCase(TestCase):
    """Test cases for 'callables'"""

    def test_x_is_callable(self):
        self.assertEqual(callable(x),False)
    def test_callable_class_is_callable(self):
        self.assertEqual(callable(CallableClass),True)
    def test_callable_instance_is_callable(self):
        self.assertEqual(callable(CallableClass()),True)
    def test_uncallable_class_is_callable(self):
        self.assertEqual(callable(UnCallableClass),True)
    def test_uncallable_instance_is_callable(self):
        self.assertEqual(callable(UnCallableClass()),False)

main()
