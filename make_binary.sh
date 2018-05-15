#!/bin/bash

mkdir binary

cython diod.py --embed
cython power.py --embed
cython box.py --embed

cp *.c binary/
cd binary
gcc `python-config --cflags --ldflags` diod.c -o diod
gcc `python-config --cflags --ldflags` power.c -o power
gcc `python-config --cflags --ldflags` box.c -o box

rm *.c
