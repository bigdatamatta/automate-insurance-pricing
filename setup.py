#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import subprocess
from typing import List

from setuptools import setup

PYTHON_VERSION="3.7"


# Return git remote url
def _git_url() -> str:
    try:
        out = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=".", universal_newlines=True)
        return out.strip()
    except subprocess.CalledProcessError:
        # git returned error, we are not in a git repo
        return ""
    except OSError:
        # git command not found, probably
        return ""


# Return Git remote in HTTP form
def _git_http_url() -> str:
    return re.sub(r".*@(.*):(.*).git", r"http://\1/\2", _git_url())

setup(
    name='automated_pricing_flow',
    version=automated_pricing_flow.__version__,
    author="Wakam",
    author_email="nassim.ezzakraoui@wakam.com",
    description="Package made to automate the pricing steps from exploration to modelling",
    url=_git_http_url(),
    license='Private usage',
    python_requires='~=' + PYTHON_VERSION,
    packages=['automated_pricing_flow']
)

