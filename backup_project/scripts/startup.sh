#!/bin/bash

./watch.sh

while true 
do
    python3 ./daily_report.py
    sleep 86400
done