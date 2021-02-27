from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

compile_flags = ['-std=c++11',  '-fopenmp'] #编译器选项
linker_flags = ['-fopenmp']

module = Extension('hello',  #要生成的动态链接库的名字
                   sources=['hello.pyx'], #包含的.pyx文件，如果还想要调用c/c++，还可以加.c/.cpp文件
                   language='c++',#默认c，建议生成c++
                   include_dirs=[numpy.get_include()], #传给gcc的-i参数 This helps to create numpypython中没有数组的概念，numpy是最接近数组的，可以当做数组来用
                   extra_compile_args=compile_flags,#传给gcc的额外编译参数，建议c++的11表
                   extra_link_args=linker_flags)#传给gcc的额外链接参数

setup(
    name='hello',
    ext_modules=cythonize(module),
    gdb_debug=False # This is extremely dangerous; Set it to False in production.
)
