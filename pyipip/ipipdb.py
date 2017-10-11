# coding: utf-8

import os
import sys
import time
import array
import struct
import logging
import platform

# speed-up attr lookup
from struct import unpack
from socket import inet_aton
from bisect import bisect_left


logger = logging.getLogger(__name__)

IS_PY3 = sys.version_info[0] == 3
IS_PYPY = platform.python_implementation() == 'PyPy'

unpack_uint32_little = lambda b: struct.unpack("<L", b)[0]
unpack_uint32_big = lambda b: struct.unpack(">L", b)[0]
unpack_uint16_big = lambda b: struct.unpack(">H", b)[0]
if IS_PY3:
    unpack_uint8 = lambda b: b
else:
    unpack_uint8 = lambda b: struct.unpack("B", b)[0]


class IPIPDatabase(object):

    def __init__(self, filename):
        self.filename = os.path.abspath(filename)
        self._ranges = array.array('I')
        self._offsets = array.array('I')
        self._strings = ''
        self.load_db()

    def __repr__(self):
        return '<IPIPDatabase filename=%r>' % (self.filename)

    def load_db(self):
        start = time.time()
        filename = self.filename
        with open(filename, 'rb') as f:
            buff = f.read()
        if filename.endswith('.dat'):
            index_size = 256 * 4
            text_length_size = 1
        elif filename.endswith('.datx'):
            index_size = 256 * 256 * 4
            text_length_size = 2
        else:
            raise Exception('unknown database format')
        self._load_db(buff, index_size, text_length_size)
        logger.debug('loaded ipip data file: %s, in %.2fs, ranges: %s',
                     filename, time.time()-start, len(self._ranges))
        if not IS_PYPY:
            logger.debug('mem usage: idx %.2fM, offsets %.2fM, strings %.2fM',
                         sys.getsizeof(self._ranges)/1048576.0,
                         sys.getsizeof(self._offsets)/1048576.0,
                         sys.getsizeof(self._strings)/1048576.0,
                        )

    def _load_db(self, buff, index_size, text_length_size):
        ns_buff = []
        ns_offset = 0
        offset_old_to_new= {}
        text_start = unpack_uint32_big(buff[:4]) - index_size
        offset = index_size + 4
        while offset < text_start:
            ip_range = unpack_uint32_big(buff[offset:offset+4])
            offset += 4
            self._ranges.append(ip_range)
            text_offset = unpack_uint32_little(buff[offset:offset+3] + b'\0') + text_start
            offset += 3
            if text_length_size == 1:
                text_length = unpack_uint8(buff[offset])
            elif text_length_size == 2:
                text_length = unpack_uint16_big(buff[offset:offset+2])
            offset += text_length_size
            if text_offset not in offset_old_to_new:
                s = buff[text_offset:text_offset+text_length].decode('utf-8')
                offset_old_to_new[text_offset] = (ns_offset, ns_offset+len(s))
                ns_buff.append(s)
                ns_offset += len(s)
            self._offsets.extend(offset_old_to_new[text_offset])
        self._strings = ''.join(ns_buff)

    def lookup(self, ip):
        n = unpack(">L", inet_aton(ip))[0]
        i = bisect_left(self._ranges, n)
        return self._strings[self._offsets[2*i]:self._offsets[2*i+1]]

