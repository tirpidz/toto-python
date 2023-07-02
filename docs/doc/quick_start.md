# Quick Start

## Prerequisites

The following sections will guide you into installing the project depedencies. The following instructions are for `ubuntu`.

Make sure you have the latest updates & required software:
```bash
sudo apt update
sudo apt install git python3 python3-pip python3-venv
```

### Git

Make sure that you setup git properly:
```bash
git config --global user.name "John Doe"
git config --global user.email john@gmail.com
git config --global pull.rebase true
```

### Git LFS

* Download [Git LFS](https://git-lfs.com/) & install `Git LFS`.
* Make sure to complete the integration with git:
```bash
git lfs install
```

## Getting the code

* Clone the repository:
```bash
git clone git@github.com:tirpidz/toto-python.git
cd toto-python
```
* Create the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
```
* Activate the virtual environment:
```bash
source venv/bin/activate
```
## IDE

Currently our preference for `IDE` is with [`vscode`](https://code.visualstudio.com/).

### vscode

The default settings & recommended extensions for the repository are under version control inside the `.vscode`.

!!! warning

    ATM with the latest version of the plugins, I'm unable to run isort on save. One has to run it manually with: `isort ./clear_vision`.
