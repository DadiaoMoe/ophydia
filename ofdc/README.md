# OFDC

OFDC is the ophydia compiler.

## Prerequisites

### Installling Python 3.6
OFDC can only be built using Python 3.6 and higher. If you are already running Python 3.6, skip to the next section, else follow the instructions here to make sure you have the correct Python version installed, and are using that version.

+ https://vyper.readthedocs.io/en/latest/installing-vyper.html

### Creating a virtual environment
```
sudo apt install virtualenv
virtualenv -p python3.6 --no-site-packages ./ofdc-venv
source ./ofdc-venv/bin/activate
```

## Installation

Again, it is strongly recommended to install OFDC in a virtual Python environment. This guide assumes you are in a virtual environment containing Python 3.6.

Get the latest version of Vyper by cloning the Github repository, and run the install and test commands:

```
git clone https://github.com/DadiaoMoe/ophydia.git
cd vyper
make
make test
```

## Compiling a contract

```
ofdc contract.oph <args>
```