import unittest
from arrs import get, my_slice

class TestUtilsArrs(unittest.TestCase):

    def test_get(self):
        array = [1, 2, 3, 4, 5]

        self.assertEqual(get(array, 0), 1)
        self.assertEqual(get(array, 1), 2)
        self.assertEqual(get(array, 2), 3)
        self.assertEqual(get(array, 3), 4)
        self.assertEqual(get(array, 4), 5)
        self.assertEqual(get(array, 5, 10), 10)
        self.assertEqual(get(array, -1), 5)
        self.assertEqual(get(array, -2), 4)
        self.assertEqual(get(array, -3), 3)
        self.assertEqual(get(array, -4), 2)
        self.assertEqual(get(array, -5), 1)
        self.assertEqual(get(array, -6, 10), 10)

    def test_my_slice(self):
        array = [1, 2, 3, 4, 5]

        self.assertEqual(my_slice(array), [1, 2, 3, 4, 5])
        self.assertEqual(my_slice(array, 1), [2, 3, 4, 5])
        self.assertEqual(my_slice(array, 2), [3, 4, 5])
        self.assertEqual(my_slice(array, 3), [4, 5])
        self.assertEqual(my_slice(array, 4), [5])
        self.assertEqual(my_slice(array, 5), [])
        self.assertEqual(my_slice(array, -1), [5])
        self.assertEqual(my_slice(array, -2), [4, 5])
        self.assertEqual(my_slice(array, -3), [3, 4, 5])
        self.assertEqual(my_slice(array, -4), [2, 3, 4, 5])
        self.assertEqual(my_slice(array, -5), [1, 2, 3, 4, 5])
        self.assertEqual(my_slice(array, 1, 3), [2, 3])
        self.assertEqual(my_slice(array, 2, 4), [3, 4])
        self.assertEqual(my_slice(array, 3, 5), [4, 5])
        self.assertEqual(my_slice(array, 1, -1), [2, 3, 4])
        self.assertEqual(my_slice(array, 2, -2), [3, 4])
        self.assertEqual(my_slice(array, 3, -3), [4])
        self.assertEqual(my_slice(array, -3, -1), [3, 4])
        self.assertEqual(my_slice(array, -4, -2), [2, 3])
        self.assertEqual(my_slice(array, -5, -3), [1, 2])
        self.assertEqual(my_slice(array, 1, 10), [2, 3, 4, 5])
        self.assertEqual(my_slice(array, 2, 10), [3, 4, 5])
        self.assertEqual(my_slice(array, 3, 10), [4, 5])
        self.assertEqual(my_slice(array, 4, 10), [5])
        self.assertEqual(my_slice(array, 5, 10), [])
        self.assertEqual(my_slice(array, -1, 10), [5])
        self.assertEqual(my_slice(array, -2, 10), [4, 5])
        self.assertEqual(my_slice(array, -3, 10), [3, 4, 5])
        self.assertEqual(my_slice(array, -4, 10), [2, 3, 4, 5])
        self.assertEqual(my_slice(array, -5, 10), [1, 2, 3, 4, 5])
        self.assertEqual(my_slice(array, 1, -5), [])
        self.assertEqual(my_slice(array, 2, -4), [])
        self.assertEqual(my_slice(array, 3, -3), [])
        self.assertEqual(my_slice(array, -3, -5), [])
        self.assertEqual(my_slice(array, -4, -4), [])
        self.assertEqual(my_slice(array, -5, -5), [])
        self.assertEqual(my_slice(array, 1, -10), [])
        self.assertEqual(my_slice(array, 2, -10), [])
        self.assertEqual(my_slice(array, 3, -10), [])
        self.assertEqual(my_slice(array, 4, -10), [])
        self.assertEqual(my_slice(array, 5, -10), [])
        self.assertEqual(my_slice(array, -1, -10), [])
        self.assertEqual(my_slice(array, -2, -10), [])
        self.assertEqual(my_slice(array, -3, -10), [])
        self.assertEqual(my_slice(array, -4, -10), [])
        self.assertEqual(my_slice(array, -5, -10), [])


if __name__ == '__main__':
    unittest.main()