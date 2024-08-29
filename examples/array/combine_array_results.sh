#!/bin/sh

cd out

# read in data 
cat inv-array-* >> final_array_result.out

# clean up by removing individual out files
rm inv-array-*.out
