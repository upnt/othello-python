from glob import glob
from os.path import basename, splitext

from setuptools import setup, find_packages

setup(
    name="othello",
    version="1.0",
    description="You can play othello",
    author="upnt",
    url="https://github.com/upnt/othello-python",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
