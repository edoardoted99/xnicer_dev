"""Installation module for XNicer.

For local tests, the recommended way of using this module is

`python setup.py build_ext --use-cython --inplace`

This requires cython in the local path.
"""

import sys
# from distutils.core import setup
# from distutils.extension import Extension
from setuptools import setup
from setuptools.extension import Extension
import numpy as np

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

if '--use-cython' in sys.argv:
    USE_CYTHON = True
    sys.argv.remove('--use-cython')
else:
    USE_CYTHON = False
EXT = '.pyx' if USE_CYTHON else '.c'

EXTENSIONS = [
    Extension(
        'xnicer.kde.kde',
        ['xnicer/kde/kde' + EXT]
    ),
    Extension(
        'xnicer.xdeconv.em_step',
        ['xnicer/xdeconv/em_step' + EXT],
        include_dirs=[np.get_include()],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp']
    )
]

if USE_CYTHON:
    from Cython.Build import cythonize
    EXTENSIONS = cythonize(EXTENSIONS)

setup(
    name='xnicer',
    version='0.2.0',
    author='Marco Lombardi',
    author_email='marco.lombardi@gmail.com',
    description='The XNICER/XNICEST algorithm',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/astropy/xnicer',
    packages=['xnicer', 'xnicer.xdeconv', 'xnicer.kde'], # was setuptools.find_packages()
    python_requires='>=3.6',
    setup_requires=['numpy', 'matplotlib', 'scipy', 'sklearn', 'astropy',
                    'nptyping'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Cython',
        'License:: OSI Approved:: GNU Lesser General Public License v3(LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    keywords='xnicer',
    ext_modules=EXTENSIONS
)
