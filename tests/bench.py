from __future__ import print_function

import gzip
import time
import logging
import resource
import socket
import os


CWD = os.path.dirname(__file__)
DATA_FILE = os.path.join(CWD, '17monipdb.dat')

# logging.basicConfig(level=logging.DEBUG)


with gzip.open(os.path.join(CWD, 'ips.gz'), 'rb') as f:
    testdata = [l.strip().decode('latin1') for l in f]


class BenchBase(object):
    pass


class Bench_official(BenchBase):

    def setup(self):
        import ipip
        self.db = ipip.IP
        self.db.load(DATA_FILE)

    def run(self):
        db = self.db
        for ip in testdata:
            db.find(ip)


class Bench_lxyu(BenchBase):

    def setup(self):
        import IP
        self.db = IP.IPv4Database(DATA_FILE)

    def run(self):
        db = self.db
        for ip in testdata:
            db.find(ip)


class Bench_pyipip(BenchBase):

    def setup(self):
        from pyipip import IPIPDatabase
        self.db = IPIPDatabase(DATA_FILE)

    def run(self):
        db = self.db
        for ip in testdata:
            db.lookup(ip)


def main():
    N = 3
    for b in BenchBase.__subclasses__():
        n = b.__name__.split('_')[1]
        c = b()
        c.setup()
        c.run() # warm-up
        s = time.time()
        for _ in range(N):
            c.run()
        e = time.time() - s
        print(n, '%.2f' % (N*len(testdata) / e))


if __name__ == '__main__':
    main()
