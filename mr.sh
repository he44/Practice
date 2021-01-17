#!/bin/bash

# make sure we have two arguments
if [ "$#" -ne 2 ]; then
    echo "Need 2 parameters, got $#"
    exit 1
fi
# get the file path
src_file_path="$PWD/$1"
run_file_path="$PWD/a.out"
in_file_path="$PWD/$2"

if [ ! -f "$src_file_path" ]; then
    echo "$src_file_path does not exist"
    exit 1
fi

if [ ! -f "$in_file_path" ]; then
    echo "$in_file_path does not exist"
    exit 1
fi

# remove the old 
if [ -f "$run_file_path" ]; then
    rm $run_file_path
fi

# compile 
clang++ $src_file_path -o $run_file_path -std=c++17 -O2 -Wall
# run
$run_file_path < $in_file_path
