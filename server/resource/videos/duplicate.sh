#!/bin/bash


files=$(ls *.mp4)


for i in $(seq 100); do
    for f in ${files}; do
        cp $f copied-${i}-${f}
    done
done
