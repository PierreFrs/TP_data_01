#!/usr/bin/env python3
"""
Générateur de rapport quotidien d'activité
"""

import os
import json
from datetime import datetime

def collect_daily_stats():
    """Collecte les statistiques du jour"""
    today = datetime.now().strftime('%Y%m%d')
    reports_dir = "data/reports"
    
    stats = {
        'date': today,
        'total_files': 0,
        'csv_files': 0,
        'txt_files': 0,
        'total_lines': 0,
        'total_words': 0,
        'file_details': []
    }
    
    # Parcourir les rapports du jour
    if os.path.exists(reports_dir):
        for filename in os.listdir(reports_dir):
            if filename.startswith(f"report_{today}") and filename.endswith('.json'):
                try:
                    with open(os.path.join(reports_dir, filename), 'r') as f:
                        report = json.load(f)
                    
                    stats['total_files'] += 1
                    
                    if report['type'] == 'CSV':
                        stats['csv_files'] += 1
                        stats['total_lines'] += report.get('data_lines', 0)
                    elif report['type'] == 'TXT':
                        stats['txt_files'] += 1
                        stats['total_words'] += report.get('total_words', 0)
                    
                    stats['file_details'].append({
                        'name': report['filename'],
                        'type': report['type'],
                        'timestamp': report['timestamp']
                    })
                    
                except Exception as e:
                    print(f"Erreur lecture rapport {filename}: {e}")
    
    return stats

def generate_daily_html(stats):
    """Génère le rapport HTML quotidien"""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Rapport Quotidien - {stats['date']}</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                margin: 0;
                background: #f0f2f5;
            }}
            .container {{
                max-width: 800px;
                margin: 20px auto;
                background: white;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .header {{
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding: 30px;
                border-radius: 10px 10px 0 0;
                text-align: center;
            }}
            .stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                padding: 30px;
            }}
            .stat-box {{
                background: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                text-align: center;
                border-left: 4px solid #667eea;
            }}
            .stat-number {{
                font-size: 2em;
                font-weight: bold;
                color: #667eea;
            }}
            .files-list {{
                padding: 0 30px 30px;
            }}
            .file-item {{
                background: #f8f9fa;
                margin: 10px 0;
                padding: 15px;
                border-radius: 5px;
                border-left: 4px solid #28a745;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Rapport Quotidien</h1>
                <p>{datetime.now().strftime('%d/%m/%Y')}</p>
            </div>
            
            <div class="stats">
                <div class="stat-box">
                    <div class="stat-number">{stats['total_files']}</div>
                    <div>Fichiers Traités</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">{stats['csv_files']}</div>
                    <div>Fichiers CSV</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">{stats['txt_files']}</div>
                    <div>Fichiers TXT</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">{stats['total_lines']:,}</div>
                    <div>Lignes Totales</div>
                </div>
            </div>
            
            <div class="files-list">
                <h2>Détail des Fichiers</h2>
    """
    
    for file_info in stats['file_details']:
        html_content += f"""
                <div class="file-item">
                    <strong>{file_info['name']}</strong> 
                    <span style="background: #007bff; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;">
                        {file_info['type']}
                    </span>
                    <div style="color: #666; font-size: 0.9em; margin-top: 5px;">
                        {file_info['timestamp']}
                    </div>
                </div>
        """
    
    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    
    # Sauvegarde
    report_file = f"data/reports/daily_report_{stats['date']}.html"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Rapport quotidien généré: {report_file}")
    return report_file

def main():
    print("=== Génération du Rapport Quotidien ===")
    
    stats = collect_daily_stats()
    
    if stats['total_files'] == 0:
        print(" Aucun fichier traité aujourd'hui")
        return
    
    report_file = generate_daily_html(stats)
    
    print(f" Rapport terminé:")
    print(f"   - {stats['total_files']} fichiers traités")
    print(f"   - {stats['csv_files']} CSV, {stats['txt_files']} TXT")
    print(f"   - Rapport: {report_file}")

if __name__ == '__main__':
    main()