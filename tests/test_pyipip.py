# coding: utf-8

from __future__ import unicode_literals
import unittest
import logging
import os

import pyipip


# logging.basicConfig(level=logging.DEBUG)

CWD = os.path.dirname(__file__)
DATA_FILE = os.path.join(CWD, '17monipdb.dat')


class TestPyIPIP(unittest.TestCase):

    def test_smoke(self):
        self.db = pyipip.IPIPDatabase(DATA_FILE)
        self.assertEqual(self.db.lookup('0.0.0.0'), u"保留地址\t保留地址\t\t")
        self.assertEqual(self.db.lookup('127.0.0.1'), u"本机地址\t本机地址\t\t")
        self.assertEqual(self.db.lookup('198.18.0.0'), u"保留地址\t保留地址\t\t")
        self.assertEqual(self.db.lookup('255.255.255.255').split()[0], u"IPIP.NET")


if __name__ == '__main__':
    unittest.main()
