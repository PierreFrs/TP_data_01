#!/bin/bash

echo "=== Mode Surveillance Activé ==="

WATCH_INTERVAL=30
SCRIPT_DIR="$(dirname "$0")"

while true; do

    echo " $(date '+%H:%M:%S') - verification des nouveaux fichiers ..."


    file_count=$(find data/work -maxdepth 1 -type f | wc -l)

    if [ $file_count -gt 0 ]; then
        echo " $file_count fichier(s) detecté(s) - lancement du script de sauvegarde"
        bash "$SCRIPT_DIR/backup.sh"
    fi

    sleep $WATCH_INTERVAL

done
