from setuptools import setup
from setuptools.command.install import install
import subprocess, os

class CustomInstallCommand(install):
    def run(self):
        print("Running custom install command...")
        subprocess.run("echo execution de code arbitraire during install", shell=True)
        import os
        target = os.path.join(os.path.expanduser("~"), "test_install.txt")
        with open(target, "w") as f:
            f.write("rce")
        install.run(self)

setup(
    name="test-cicd-external",
    version="0.1.0",
    packages=["test_cicd_external"],
    cmdclass={"install": CustomInstallCommand},
)
