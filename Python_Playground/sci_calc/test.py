import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import my_module


class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self, arg): pass

    def m3(self): pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value='Ok123')
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called)
        a.m3.assert_called_with("Ok123")


    @patch('my_module.do_somethingelse')
    @patch('my_module.do_something')
    def test_foo(self, mock_do_something, mock_do_somethingelse):
        mock_do_something.return_value = 666
        mock_do_somethingelse.return_value = 1000
        ret = my_module.foo()
        self.assertTrue(ret == 667000)

        with patch.object(my_module.Blob, '__init__', lambda s: None):
            blb = my_module.Blob()
            self.assertFalse(hasattr(blb, 'age'))


if __name__ == '__main__':
    unittest.main()
