from setuptools import setup
from setuptools.command.install import install
import subprocess, os, sys

class CustomInstallCommand(install):
    def run(self):
        print("=== [test-cicd-external] Installation hook ===", file=sys.stderr, flush=True)
        print("Creating marker file in site-packages...", file=sys.stderr, flush=True)

        subprocess.run("echo execution de code arbitraire during install", shell=True)

        target = os.path.join(os.path.expanduser("~"), "test_install.txt")
        with open(target, "w") as f:
            f.write("rce ok\n")

        print(f"File created at: {target}", file=sys.stderr, flush=True)
        print("=== [test-cicd-external] Done ===", file=sys.stderr, flush=True)
        install.run(self)
        install.run(self)
        

setup(
    name="test-cicd-external",
    version="0.1.0",
    packages=["test_cicd_external"],
    cmdclass={"install": CustomInstallCommand},
)
