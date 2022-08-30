#!/bin/bash

#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v var=$nuc '/^#/{next} {if ($4 == var) {print $5}}' $1 | sort | uniq -c
done
