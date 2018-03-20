# Anti-Duplicator

This script searches directory _default_ in current working directory and find file duplicates in it
Two files are considered duplicate, if they have same name and same size. Content may be different.

You can specify input directory with parameter __-p__ or __--path__

# Quickstart

Example of script launch on Linux, __Python 3.5__:

```bash

$ python3 duplicates.py -p dupe-test
Found coincidence between files:
dupe-test/1.txt
dupe-test/inside/1.txt
dupe-test/inside/deeper/deepest/1.txt
Found coincidence between files:
dupe-test/2.txt
dupe-test/inside/deeper/deepest/2.txt


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
