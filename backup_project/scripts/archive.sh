#! /bin/bash

DATE=$(date +"%d-%m-%Y - %HH:%MM:%SS")

tar -cfz ../data/backup-"$DATE".tar.gz ../data/archives
if [ -f ../data/backup-"$DATE".tar.gz ]; then
    rm -r ../data/backup/*
fi