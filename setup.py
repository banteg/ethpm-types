#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup  # type: ignore

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "pytest>=6.0,<7.0",  # Core testing package
        "pytest-xdist",  # multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
        # Test-only deps
        "PyGithub>=1.54,<2.0",  # Necessary to pull official schema from github
        "hypothesis-jsonschema==0.19.0",  # Fuzzes based on a json schema
    ],
    "lint": [
        "black>=22.3.0,<23.0",  # auto-formatter and linter
        "mypy>=0.950,<1.0",  # Static type analyzer
        "types-PyYAML",  # NOTE: Needed due to mypy typeshed
        "types-requests",  # NOTE: Needed due to mypy typeshed
        "flake8>=3.9.2,<4.0",  # Style linter
        "flake8-breakpoint>=1.1.0,<2.0.0",  # detect breakpoints left in code
        "flake8-print>=4.0.0,<5.0.0",  # detect print statements left in code
        "isort>=5.10.1,<6.0",  # Import sorting linter
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen>=2.19,<2.20",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to committing
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="ethpm-types",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""ethpm_types: Implementation of EIP-2678""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ApeWorX Ltd.",
    author_email="admin@apeworx.io",
    url="https://github.com/ApeWorX/ethpm-types",
    include_package_data=True,
    install_requires=[
        "importlib-metadata ; python_version<'3.8'",
        "typing_extensions ; python_version<'3.8'",
        "hexbytes>=0.2.2,<0.3",
        "pydantic>=1.8.2,<2.0.0",
        "eth-utils>=1.10.0,<3.0",
        "py-cid>=0.3.0,<0.4.0",
    ],
    python_requires=">=3.7.2,<3.11",
    extras_require=extras_require,
    py_modules=["ethpm_types"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ethpm_types": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
