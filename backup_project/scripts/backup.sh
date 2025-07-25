#! /bin/bash

# FULL file name #
FILE=$1
# Extract file 'name' only
FILENAME="${FILE%.*}"
# Extract file 'extension' only
EXTENSION="${FILE##*.}"
DATE=$(date +"%d-%m-%Y - %HH:%MM:%SS")

# analyze .csv/.txt files
if [ ! "$EXTENSION" = "txt" ] || [ ! "$EXTENSION" = "csv" ]; then
    ls -lh "$FILE" >> ../logs/file_stats-"$DATE".txt
else
    ./analyze >> ../logs/file_stats-"$DATE".txt
fi

# copy files w/ date from data/work
cp ../data/work/"$FILE" ../data/backup/"$FILENAME-$DATE.$EXTENSION" >> ../logs/file_stats-"$DATE".txt