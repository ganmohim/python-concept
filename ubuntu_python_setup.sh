#!/bin/bash
#############################################################################
# On a clean Ubuntu machine this should help to have Python3.7 setup
# Author: GAN MOHIM
# Copyright (c) 2019, GAN MOHIM
#############################################################################

sudo apt-get update

# good to have though not tied to py3
sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev

sudo apt-get install python3.7

# Details: https://stackoverflow.com/questions/26053982/setup-script-exited-with-error-command-x86-64-linux-gnu-gcc-failed-with-exit
# Without this you can't pip install things like orderedset
sudo apt-get install python3.7-dev

# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# For you to discover:  Please read Python doc came with get-pip.py
python get-pip.py


# This is only you have multiple Python version else skip
# Shows usage of update-alternatives to set default Python version
# Linux man page should suffice
# update-alternatives --help
# update-alternatives --display python