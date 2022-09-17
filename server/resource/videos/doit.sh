#!/bin/bash


origs=$(ls *.mp4)


for i in $(seq 100); do
    for f in ${origs}; do
        cp ${f} copied-${i}-${f}
    done
done
