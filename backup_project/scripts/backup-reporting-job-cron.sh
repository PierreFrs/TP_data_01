#!/bin/bash

CURRENT_DIR="$(pwd)"
CRON_JOB="0 0 * * * cd $CURRENT_DIR && ./backup-reporting-job-cron.sh"

(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -