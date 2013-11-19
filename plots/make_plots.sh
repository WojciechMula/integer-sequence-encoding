#!/bin/sh

python gen_gnuplot.py

for f in *.gnuplot
do
	gnuplot "$f"
done
