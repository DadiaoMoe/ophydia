# OFDC

OFDC is the ophydia compiler.

## Prerequisites

### Installling Python 3.6
OFDC can only be built using Python 3.6 and higher.

### Creating a virtual environment
```
sudo apt install virtualenv
virtualenv -p python3.6 --no-site-packages ~/ofdc-venv
source ~/ofdc-venv/bin/activate
```

## Installation

Again, it is strongly recommended to install OFDC in a virtual Python environment. This guide assumes you are in a virtual environment containing Python 3.6.

Get the latest version of Vyper by cloning the Github repository, and run the install and test commands:

```
git clone https://github.com/DadiaoMoe/ophydia.git
cd ophydia
make
make test
```

## Compiling a contract

```
ofdc contract.oph <args>
```
