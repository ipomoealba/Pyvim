#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import errno
import subprocess
import platform
try:
    os.rename('/etc/foo', '/etc/bar')
except IOError as e:
    if (e[0] == errno.EPERM):
        print("You need root permissions to do this, laterz!")
        sys.exit(1)

subprocess.call(
    "wget clone https://raw.githubusercontent.com/ipomoealba/Pyvim/master/.vimrc ~/.vimrc")

if "Darwin" in platform.platform():
    if subprocess.check_call("brew --version") == 0:
        print("You have install Homebrew")
    else:
        subprocess.call(
            "/usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
    subprocess.call("brew install Cmake")
elif "Ubuntu" in "".join(platform.uname()):
    subprocess.call("apt-get install build-essential cmake")

subprocess.call("vim")
subprocess.call("cd ~/.vim/plugged/YouCompleteMe && ./install.py --all")
