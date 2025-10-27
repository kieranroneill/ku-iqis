<h1 align="center">
  Introduction to Quantum Information Science: Poster Presentation
</h1>

---

### Table of contents

* [1. Getting started](#-1-getting-started)
  - [1.1. Prerequisites](#11-prerequisites)
  - [1.2. Installation](#12-installation)
* [2. Data analysis](#-2-data-analysis)
* [3. Appendix](#-3-appendix)
  - [3.1. Useful commands](#31-useful-commands)

## 🪄 1. Getting Started

### 1.1. Prerequisites

* [Git LFS](https://github.com/git-lfs/git-lfs#installing)
* [Make (optional)](https://www.gnu.org/software/make/)
* [Python (3.10.12+)](https://www.python.org/downloads/)
* [Pip](https://pip.pypa.io/en/stable/installation/)

### 1.2. Installation

First, create the virtual environment:

```shell
python3 -m venv .venv
```

Next, activate the virtual environment and install the dependencies to it:

```shell
source .venv/bin/activate && \
    pip install -r pip-requirements.txt && \
    pip install -r dev-requirements.txt && \
    pip install -r requirements.txt && \
    pre-commit install && \
    deactivate
```

> ⚠️ **NOTE:** There are three `pip` dependency lock files:
> * `pip-requirements.txt` - locks down the version of `pip` within the virtual environment.
> * `dev-requirements.txt` - contains the necessary development dependencies, such as `black`, `flake8`, `isort`, and `pre-commit` that are not strictly necessary to run the project, but provide utility.
> * `requirements.txt` - contains the necessary dependencies for the project.

Alternatively, if Make is installed, simply run:

```shell
make install
```

> ⚠️ **NOTE:** This repository requires Git LFS to be installed. If the repository is cloned without Git LFS, install LFS and run `git lfs pull` to fetch the data.

<sup>[Back to top ^][table-of-contents]</sup>

## 📊 2. Data analysis

<sup>[Back to top ^][table-of-contents]</sup>

## 📑 3. Appendix

### 3.1. Useful commands

| Command            | Description                                                                                                               |
|--------------------|---------------------------------------------------------------------------------------------------------------------------|
| `make format`      | Formats all Python/Jupyter files. <br/><br/> ⚠️ **NOTE:** This is write action and will update the Python files in-place. |
| `make install`     | Installs all Python dependencies, via `pip` into a virtual environment `.venv`.                                           |
| `make lint`        | Runs the linter on the Python/Jupyter files.                                                                              |
| `make run_electro` | Runs the Jupyter notebook file for the electro lab data analysis.                                                         |
| `make run_physics` | Runs the Jupyter notebook file for the physics lab data analysis.                                                         |

<sup>[Back to top ^][table-of-contents]</sup>

<!-- links -->
[table-of-contents]: #table-of-contents
