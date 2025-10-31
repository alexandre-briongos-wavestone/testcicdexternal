# setup.py
from setuptools import setup
import subprocess

subprocess.run(["echo", "execution de code arbitraire during install"], shell=True)
with open("rce.txt", "w") as f:
    f.write("rce")
setup()
