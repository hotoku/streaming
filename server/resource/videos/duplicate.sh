#!/bin/bash


files=$(ls *.mp4 | grep -v copied)


for i in $(seq 100); do
    for f in ${files}; do
        cp $f copied-あいうえお-${i}-${f}
    done
done
