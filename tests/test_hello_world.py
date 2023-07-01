import unittest
from toto import hello_world


class TestHelloWorld(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(hello_world.magic_number(),
                         42,
                         'The magic is working.')


if __name__ == '__main__':
    unittest.main()
