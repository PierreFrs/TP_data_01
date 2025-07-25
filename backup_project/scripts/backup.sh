#!/bin/bash

FILE=$1
FILENAME="${FILE%.*}"
EXTENSION="${FILE##*.}"
DATE=$(date +"%Y-%m-%d_%Hh%Mm%Ss")

# Log file paths
LOG_FILE="../logs/backup_logs-$DATE.txt"

# Function to log with timestamp
log_action() {
    local message="$1"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] - $message" >> "$LOG_FILE"
}

# Create logs directory if it doesn't exist
mkdir -p ../logs

# Log script start
log_action "STARTED: Archive script for file: $FILE"

# Create stats file and log the action
if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
    log_action "CREATED: Stats log file: $LOG_FILE"
fi

# Analyze files and log the action
if [ "$EXTENSION" != "txt" ] && [ "$EXTENSION" != "csv" ]; then
    log_action "ANALYZING: Running stat command on $FILE (non-text file)"
    stat "../data/work/$FILE" >> "$LOG_FILE"
    log_action "COMPLETED: Stat analysis written to $LOG_FILE"
else
    log_action "ANALYZING: Running Python analysis on $FILE (text/csv file)"
    python3 analyze.py "$FILE" >> "$LOG_FILE"
    log_action "COMPLETED: Python analysis written to $LOG_FILE"
fi

# Log the copy operation
log_action "COPYING: $FILE from work to backup directory"

# Perform copy and log result
if cp "../data/work/$FILE" "../data/backup/$FILENAME-$DATE.$EXTENSION" 2>> "$LOG_FILE"; then
    log_action "SUCCESS: File copied to ../data/backup/$FILENAME-$DATE.$EXTENSION"
else
    log_action "ERROR: Failed to copy $FILE to backup directory"
    exit 1
fi

log_action "FINISHED: Archive script completed for $FILE"