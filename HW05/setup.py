from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('C_mul.pyx'))
setup(ext_modules = cythonize('Cython_mul.pyx'))
# python3 setup.py build_ext --inplace