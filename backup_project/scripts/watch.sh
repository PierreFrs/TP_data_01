#!/bin/bash

DIRECTORY="../data/work/"

while true
do
    echo "Checking work directory..."
    if [ "$(ls -A $DIRECTORY 2>/dev/null)" ]; then
        echo "Files detected, launching jobs..."
        for f in "$DIRECTORY"*.* ; do
            [[ -e "$f" ]] || break
            filename=$(basename "$f")
            echo "Processing: $filename"
            ./backup.sh "$filename"
        done
    else
        echo "No file detected in work directory"
    fi
    sleep 30
done