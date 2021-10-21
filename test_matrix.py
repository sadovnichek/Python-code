from matrix import Matrix
import unittest


class TestMatrix(unittest.TestCase):
    def test_add(self):
        a = Matrix([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
        b = Matrix([[0, 0, 3],
                    [0, 0, 0],
                    [3, 0, 0]])
        result = Matrix([[1, 0, 3],
                         [0, 1, 0],
                         [3, 0, 1]])
        self.assertEqual(a + b, result)
