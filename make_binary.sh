#!/bin/bash

mkdir binary
# Convert Python code to C
cython diod.py --embed
cython power.py --embed
cython box.py --embed

cp *.c binary/
rm *.c
cd binary
# Make binary file from .c files
gcc $(python-config --cflags) ./diod.c $(python-config --ldflags) -o diod
gcc $(python-config --cflags) ./power.c $(python-config --ldflags) -o power
gcc $(python-config --cflags) ./box.c $(python-config --ldflags) -o box

rm *.c
