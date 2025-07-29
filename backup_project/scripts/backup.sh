#!/bin/bash

echo "=== Debut de la sauvegarde ==="

WORK_DIR="data/work"
BACKUP_DIR="data/backup"
REPORTS_DIR="data/reports"
LOG_FILE="logs/backup_$(date +%Y%m%d).log"

log_message(){
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log_message "Demarrage du processus de backup"

files_backed_up=0
total_size=0

for file in "$WORK_DIR"/*;do

    if [ -f "$file" ];then
    
        filename=$(basename "$file")
        timestamp=$(date +%Y%m%d_%H%M%S)
        backup_name="${timestamp}_${filename}"

        cp "$file" "$BACKUP_DIR/$backup_name"

        size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo 0)
        total_size=$((total_size + size))
        files_backed_up=$((files_backed_up + 1))

        log_message "Sauvegardé : $filename -> $backup_name"

        if [[ "$filename" =~ \.(csv|txt)$ ]]; then
            log_message "Analyse du fichier : $filename"
            python3 scripts/analyze.py "$file" "$REPORTS_DIR"
        fi
    
    fi

done

find "$BACKUP_DIR" -type f -mtime +30 -delete 2>/dev/null

log_message "=== resumé ==="
log_message "Fichiers sauvegardés : $files_backed_up"
log_message "Taille total $total_size octets"
log_message "Fin du processus"

echo "Sauvegarde terminée - $files_backed_up fichier(s) traité(s)"

