# Ophydia

Pythonic smart contract language for [BVM]().

## Prerequisites

### Installling Python 3.6
Ophydia can only be built using Python 3.6 and higher.

### Creating a virtual environment
```
sudo apt install virtualenv
virtualenv -p python3.6 --no-site-packages ~/ophydia-venv
source ~/ophydia-venv/bin/activate
```

## Installation

It is strongly recommended to install Ophydia in a virtual Python environment. This guide assumes you are in a virtual environment containing Python 3.6.

Get the latest version of Ophydia by cloning the Github repository, and run the install and test commands:

```
git clone https://github.com/DadiaoMoe/ophydia.git
cd ophydia
make
make test
```

## Compiling a contract

```
ophydia contract.oph <args>
```


## Documentations

See [Docs](docs/).