import os
import tempfile
import shutil
import setuptools
from distutils.core import setup


env_dir = tempfile.mkdtemp(prefix='protondate-install-')
shutil.copytree(os.path.abspath(os.getcwd()), os.path.join(env_dir, 'protondate'))

os.chdir(env_dir)

setup(
    name='protondate',
    author='velvetx',
    url='https://github.com/velvetxq/protondate',
    packages=setuptools.find_packages(),
    package_data={
        'protondate': ['*']
    },
    entry_points={
        'console_scripts': ['protondate=protondate.protondate:ProtonDate']
    }
)
