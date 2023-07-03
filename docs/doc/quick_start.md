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

## Running the scripts

The repository has examples files provided in the `examples` folder. Before running the following scripts, make you that the `venv` created in the previous step has been activated.

### FA extraction

 In order to run the FA extraction scripts run the following command:

```bash
python3 ./toto/FA_extraction.py --data="/PATH_TO_REPOSITORY/examples/input/dwi_b1000.nii.gz" --bval="/PATH_TO_REPOSITORY/examples/input/bval_1000" --bvec="/PATH_TO_REPOSITORY/examples/input/bvec_1000" --output="/PATH_TO_REPOSITORY/examples/output/tensor_fa.nii.gz"
```
Where `PATH_TO_REPOSITORY` is the local path where you cloned the repository.

## IDE

Currently our preference for `IDE` is with [`vscode`](https://code.visualstudio.com/).

### vscode

The default settings & recommended extensions for the repository are under version control inside the `.vscode`.

!!! warning

    ATM with the latest version of the plugins, I'm unable to run isort on save. One has to run it manually with: `isort ./toto`.

### Format & Checks

If you want to manually format the codebase & run the synthax checks, the `tools` folder at the root of the repository.

To format simply run the following command:
```bash
(venv) ➜  toto-python git:(feat/checks) ./tools/format.sh       
🔨 Code Formating ...
All done! ✨ 🍰 ✨
2 files left unchanged.
💫 Code Formating done.
```

To check for errors and warnings run the following command:
```bash
To format simply run the following command:
```bash
(venv) ➜  toto-python git:(feat/checks) ./tools/check.sh 
🛸 Checking Code Formating ...
All done! ✨ 🍰 ✨
2 files would be left unchanged.
💫 Checking Code Formating done.
🛸 Code Analysis ...
💫 Code Analysis done
```
