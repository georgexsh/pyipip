# coding: utf-8

from __future__ import unicode_literals
import unittest
import logging
import os

import pyipip


# logging.basicConfig(level=logging.DEBUG)

CWD = os.path.dirname(__file__)
DAT_FILE = os.path.join(CWD, '17monipdb.dat')
DATX_FILE = os.path.join(CWD, '17monipdb.datx')


class TestPyIPIP(unittest.TestCase):

    def test_dat(self):
        self.check(DAT_FILE)

    def test_datx(self):
        self.check(DATX_FILE)

    def check(self, db_file):
        db = pyipip.IPIPDatabase(db_file)
        self.assertEqual(db.lookup('0.0.0.0'), u"保留地址\t保留地址\t\t")
        self.assertEqual(db.lookup('127.0.0.1'), u"本机地址\t本机地址\t\t")
        self.assertEqual(db.lookup('198.18.0.0'), u"保留地址\t保留地址\t\t")
        self.assertIn('北京', db.lookup('202.112.80.106'))
        self.assertEqual(db.lookup('255.255.255.255').split()[0], u"IPIP.NET")


if __name__ == '__main__':
    unittest.main()
