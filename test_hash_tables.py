import hash_tables
import hash_functions
import unittest


class TestHashTables(unittest.TestCase):

    def test_linear_probe_add_ascii(self):
        ht = hash_tables.LinearProbe(2, hash_functions.h_ascii)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)
        self.assertEqual(ht.add('key3', 'v3'), False)

    def test_linear_probe_search_ascii(self):
        ht = hash_tables.LinearProbe(97, hash_functions.h_ascii)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_linear_probe_add_rolling(self):
        ht = hash_tables.LinearProbe(2, hash_functions.h_rolling)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)
        self.assertEqual(ht.add('key3', 'v3'), False)

    def test_linear_probe_search_rolling(self):
        ht = hash_tables.LinearProbe(97, hash_functions.h_rolling)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_linear_probe_add_hasCode(self):
        ht = hash_tables.LinearProbe(2, hash_functions.h_hasCode)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)
        self.assertEqual(ht.add('key3', 'v3'), False)

    def test_linear_probe_search_hasCode(self):
        ht = hash_tables.LinearProbe(97, hash_functions.h_hasCode)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_quadratic_add_ascii(self):
        ht = hash_tables.QuadraticProbe(2, hash_functions.h_ascii)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)
        self.assertEqual(ht.add('key3', 'v3'), False)

    def test_quadratic_probe_search_ascii(self):
        ht = hash_tables.QuadraticProbe(97, hash_functions.h_ascii)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_quadratic_probe_add_rolling(self):
        ht = hash_tables.QuadraticProbe(2, hash_functions.h_rolling)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)
        self.assertEqual(ht.add('key3', 'v3'), False)

    def test_quadratic_probe_search_rolling(self):
        ht = hash_tables.QuadraticProbe(97, hash_functions.h_rolling)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_quadratic_probe_add_hasCode(self):
        ht = hash_tables.QuadraticProbe(2, hash_functions.h_hasCode)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)
        self.assertEqual(ht.add('key3', 'v3'), False)

    def test_quadratic_probe_search_hasCode(self):
        ht = hash_tables.QuadraticProbe(97, hash_functions.h_hasCode)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_chained_hash_add_ascii(self):
        ht = hash_tables.ChainedHash(2, hash_functions.h_ascii)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)

    def test_chained_hash_search_ascii(self):
        ht = hash_tables.ChainedHash(97, hash_functions.h_ascii)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_chained_hash_add_rolling(self):
        ht = hash_tables.ChainedHash(2, hash_functions.h_rolling)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)

    def test_chained_hash_search_rolling(self):
        ht = hash_tables.ChainedHash(97, hash_functions.h_rolling)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)

    def test_chained_hash_add_hasCode(self):
        ht = hash_tables.ChainedHash(2, hash_functions.h_hasCode)
        self.assertEqual(ht.add('key1', 'v1'), True)
        self.assertEqual(ht.add('key2', 'v2'), True)

    def test_chained_hash_search_hasCode(self):
        ht = hash_tables.ChainedHash(97, hash_functions.h_hasCode)
        ht.add('key1', 'v1')
        ht.add('key2', 'v2')
        self.assertEqual(ht.search('key1'), 'v1')
        self.assertEqual(ht.search('key2'), 'v2')
        self.assertEqual(ht.search('key400'), None)


if __name__ == '__main__':
    unittest.main()
