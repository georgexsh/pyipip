from setuptools import setup


def read_readme():
    with open('README.rst', 'rb') as f:
        return f.read().decode('utf-8')


setup(name='pyipip',
      version='0.1.1',
      description="ipip.net IP address geolocation database Python library",
      long_description=read_readme(),
      url='https://github.com/georgexsh/pyipip',
      author='georgexsh',
      author_email='georgexsh@gmail.com',
      license='MIT',
      packages=['pyipip'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
     )
