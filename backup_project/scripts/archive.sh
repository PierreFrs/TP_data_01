#!/bin/bash

DATE=$(date +"%Y-%m-%d_%Hh%Mm%Ss")
ARCHIVE_PATH="../data/archives/backup-$DATE.tar.gz"
# Log file paths
LOG_FILE="../logs/archive_logs-$DATE.txt"

# Function to log with timestamp
log_action() {
    local message="$1"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] - $message" >> "$LOG_FILE"
}

log_action "Creating archive: $ARCHIVE_PATH"
tar -czf "$ARCHIVE_PATH" "../data/backup"

if [ $? -eq 0 ] && [ -f "$ARCHIVE_PATH" ]; then
    log_action "Archive created successfully. Cleaning backup directory..."
    rm -rf ../data/backup/*
    log_action "Backup directory cleaned."
else
    log_action "Archive creation failed. Backup directory not cleaned."
    exit 1
fi