#!/usr/bin/env python3
"""
Script d'analyse simple pour fichiers CSV et TXT
"""

import sys
import os
from datetime import datetime
import json

def analyze_csv(file_path):
    """Analyse basique d'un fichier CSV"""
    stats = {
        'type': 'CSV',
        'filename': os.path.basename(file_path),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        stats['total_lines'] = len(lines)
        
        if lines:
            # Analyser l'en-tête
            header = lines[0].strip()
            stats['columns'] = len(header.split(','))
            stats['header'] = header.split(',')
            
            # Compter les lignes de données
            stats['data_lines'] = len(lines) - 1
            
            # Détecter les lignes vides
            empty_lines = sum(1 for line in lines if not line.strip())
            stats['empty_lines'] = empty_lines
        
        print(f"Analyse CSV terminée: {stats['data_lines']} lignes de données")
        
    except Exception as e:
        stats['error'] = str(e)
        print(f"Erreur analyse CSV: {e}")
    
    return stats

def analyze_txt(file_path):
    """Analyse basique d'un fichier TXT"""
    stats = {
        'type': 'TXT',
        'filename': os.path.basename(file_path),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Statistiques basiques
        stats['total_chars'] = len(content)
        stats['total_lines'] = len(content.splitlines())
        stats['total_words'] = len(content.split())
        
        # Mots les plus fréquents (top 5)
        words = content.lower().split()
        word_count = {}
        for word in words:
            # Nettoyer les mots (enlever ponctuation basique)
            clean_word = word.strip('.,!?;:"()[]{}')
            if len(clean_word) > 2:  # Ignorer les mots trop courts
                word_count[clean_word] = word_count.get(clean_word, 0) + 1
        
        # Top 5 des mots
        top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
        stats['top_words'] = top_words
        
        print(f"Analyse TXT terminée: {stats['total_words']} mots")
        
    except Exception as e:
        stats['error'] = str(e)
        print(f"Erreur analyse TXT: {e}")
    
    return stats

def generate_report(stats, reports_dir):
    """Génère un rapport simple"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = os.path.join(reports_dir, f"report_{timestamp}_{stats['filename']}.json")
    
    # Sauvegarde JSON
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    # Rapport HTML simple
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rapport - {stats['filename']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ background: #4CAF50; color: white; padding: 20px; }}
            .content {{ padding: 20px; }}
            .stat {{ margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Rapport d'Analyse</h1>
            <p>Fichier: {stats['filename']} | {stats['timestamp']}</p>
        </div>
        <div class="content">
    """
    
    if stats['type'] == 'CSV':
        html_content += f"""
            <h2>Analyse CSV</h2>
            <div class="stat"><strong>Lignes totales:</strong> {stats.get('total_lines', 0)}</div>
            <div class="stat"><strong>Colonnes:</strong> {stats.get('columns', 0)}</div>
            <div class="stat"><strong>Lignes de données:</strong> {stats.get('data_lines', 0)}</div>
            <div class="stat"><strong>En-tête:</strong> {', '.join(stats.get('header', []))}</div>
        """
    elif stats['type'] == 'TXT':
        html_content += f"""
            <h2>Analyse Texte</h2>
            <div class="stat"><strong>Caractères:</strong> {stats.get('total_chars', 0)}</div>
            <div class="stat"><strong>Lignes:</strong> {stats.get('total_lines', 0)}</div>
            <div class="stat"><strong>Mots:</strong> {stats.get('total_words', 0)}</div>
            <div class="stat"><strong>top Mots:</strong> {stats.get('top_words', 0)}</div>
            <h3>Mots les plus fréquents:</h3>
            <ul>
        """
        for word, count in stats.get('top_words', []):
            html_content += f"<li>{word}: {count} fois</li>"
        html_content += "</ul>"
    
    html_content += """
        </div>
    </body>
    </html>
    """
    
    # Sauvegarde HTML
    html_file = os.path.join(reports_dir, f"report_{timestamp}_{stats['filename']}.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Rapport généré: {os.path.basename(html_file)}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 analyze.py <fichier> <dossier_rapports>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    reports_dir = sys.argv[2]
    
    # Créer le dossier de rapports
    os.makedirs(reports_dir, exist_ok=True)
    
    # Déterminer le type de fichier et analyser
    filename = os.path.basename(file_path).lower()
    
    if filename.endswith('.csv'):
        stats = analyze_csv(file_path)
    elif filename.endswith('.txt'):
        stats = analyze_txt(file_path)
    else:
        print(f"Type de fichier non supporté: {filename}")
        sys.exit(1)
    
    # Générer le rapport
    generate_report(stats, reports_dir)
    print("Analyse terminée avec succès")

if __name__ == '__main__':
    main()