import unittest
import cutils
import numpy as np
import io
from unittest import mock
import time
from multiply import multiply


class TestMultiplication(unittest.TestCase):
    def test_multiply(self):
        # define random shape
        m = np.random.randint(1, 10)
        n = np.random.randint(1, 10)
        k = np.random.randint(1, 10)

        left_matrix = np.random.random(size=[m, n])
        right_matrix = np.random.random(size=[n, k])

        start_capi = time.time()
        result = cutils.multiply_matrix(left_matrix, left_matrix.shape[0], left_matrix.shape[1],
                                        right_matrix, right_matrix.shape[0], right_matrix.shape[1])
        end_capi = time.time()

        start_numpy = time.time()
        true_result = np.dot(left_matrix, right_matrix)
        end_numpy = time.time()

        start_py = time.time()
        python_result = multiply(left_matrix, right_matrix)
        end_py = time.time()

        print(f"CAPI time: {end_capi - start_capi}")
        print(f"Numpy time: {end_numpy - start_numpy}")
        print(f"Python time: {end_py - start_py}")

        self.assertEqual(type(result), type(true_result))
        self.assertEqual(result.all(), true_result.all())
        self.assertEqual(python_result.all(), true_result.all())

    def test_invalid_input(self):

        m = np.random.randint(1, 10)
        n = np.random.randint(1, 10)
        p = np.random.randint(11, 20)
        k = np.random.randint(1, 10)

        left_matrix = np.random.random(size=[m, n])
        right_matrix = np.random.random(size=[p, k])

        with self.assertRaises(SystemError):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()):
                result = cutils.multiply_matrix(left_matrix, left_matrix.shape[0], left_matrix.shape[1],
                                                right_matrix, right_matrix.shape[0], right_matrix.shape[1])


if __name__ == '__main__':
    unittest.main()
