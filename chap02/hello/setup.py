from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

compile_flags = ['-std=c++11',  '-fopenmp'] #编译器选项
linker_flags = ['-fopenmp']

module = Extension('hello',  #包的名字
                   ['hello.pyx'], #一般常用.pyx后缀名
                   language='c++',#建议生成c++
                   include_dirs=[numpy.get_include()], # This helps to create numpypython中没有数组的概念，numpy是最接近数组的，可以当做数组来用
                   extra_compile_args=compile_flags,#建议c++的11表
                   extra_link_args=linker_flags)

setup(
    name='hello',
    ext_modules=cythonize(module),
    gdb_debug=True # This is extremely dangerous; Set it to False in production.
)
