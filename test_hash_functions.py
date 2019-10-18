import unittest
import hash_functions


class TestHashFunctions(unittest.TestCase):

    def test_h_ascii_key_None(self):
        with self.assertRaises(TypeError) as ex:
            r = hash_functions.h_ascii(None, 5)

        self.assertEqual(str(ex.exception), 'key is not a string')

    def test_h_ascii_key_num(self):
        with self.assertRaises(TypeError) as ex:
            r = hash_functions.h_ascii(1000, 5)

        self.assertEqual(str(ex.exception), 'key is not a string')

    def test_h_ascii_key_list(self):
        with self.assertRaises(TypeError) as ex:
            r = hash_functions.h_ascii([1, 1, 1], 5)

        self.assertEqual(str(ex.exception), 'key is not a string')

    def test_h_ascii_N_None(self):
        with self.assertRaises(TypeError) as ex:
            r = hash_functions.h_ascii('key', None)

        self.assertEqual(str(ex.exception), 'N is not an integer')

    def test_h_ascii_N_str(self):
        with self.assertRaises(TypeError) as ex:
            r = hash_functions.h_ascii('key', 'N')

        self.assertEqual(str(ex.exception), 'N is not an integer')

    def test_h_ascii_N_list(self):
        with self.assertRaises(TypeError) as ex:
            r = hash_functions.h_ascii('key', [1, 1, 1])

        self.assertEqual(str(ex.exception), 'N is not an integer')

    def test_h_ascii_index_one(self):
        r = hash_functions.h_ascii('key', 1)
        self.assertEqual(r, 0)

    def test_h_ascii_index_100(self):
        # k=107, e=101, y=121; =329
        r = hash_functions.h_ascii('key', 97)
        self.assertEqual(r, 38)

    def test_h_ascii_N_is_zero(self):
        with self.assertRaises(ZeroDivisionError) as ex:
            r = hash_functions.h_ascii('key', 0)

        self.assertEqual(str(ex.exception), 'N cannot be zero')

    def test_h_rolling_index_one(self):
        r = hash_functions.h_rolling('key', 1)
        self.assertEqual(r, 0)

    def test_h_rolling_index_100(self):
        r = hash_functions.h_rolling('key', 97)
        self.assertEqual(r, 29)

    def test_h_hasCode_index_one(self):
        r = hash_functions.h_hasCode('key', 1)
        self.assertEqual(r, 0)

    def test_h_hasCode_index_100(self):
        r = hash_functions.h_hasCode('key', 97)
        self.assertEqual(r, 52)


if __name__ == '__main__':
    unittest.main()
