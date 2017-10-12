PyIPIP
======

Description
-----------

ipip.net IPv4 地址归属地数据库 Python 查询库。同时支持 dat 与 datx
格式的数据文件，支持 Python 2 与 3。 需要先去 `ipip.net
官方网站 <http://www.ipip.net/>`__ 下载数据文件。

性能较官方库为高，在 E5-2682 2.5GHz 下 QPS 约为 490k。

Usage
-----

.. code:: python

    >>> from pyipip import IPIPDatabase
    >>> db = IPIPDatabase('/path/to/your/ipipdb.dat')
    >>> db.lookup('202.112.80.106')
    '中国\t北京\t北京\t'

Install
~~~~~~~

::

    pip install pyipip

Test & Benchmark
~~~~~~~~~~~~~~~~

::

    make test

::

    make bench

Note
----

数据文件时时更新，请自行下载使用，代码仓库随附的数据文件只用于测试。
