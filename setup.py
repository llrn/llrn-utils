from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = "LLRN Standard Python Distribution",
    version = "0.1.0",
    install_requires = required
    # ...
)